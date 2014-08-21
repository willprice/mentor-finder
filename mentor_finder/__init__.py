# -*- coding: utf-8 -*-
from flask import Flask
from flask_wtf import CsrfProtect

import mentor_finder.views
from mentor_finder.views.mentor_finder_views import MentorFinderViews
from mentor_finder.web_controller import Controller
from mentor_finder.models.mailers import StubMailer, Mailer


class MentorFinder(object):
    def __init__(self, secret_key="Super secret key", test=False):
        self.app = Flask(__name__)
        self.app.secret_key = secret_key

        if test:
            self.app.config['TESTING'] = True
            mailer_cls = StubMailer
        else:
            mailer_cls = Mailer

        self.controller = Controller(self.app,
                                     activation_mailer=mailer_cls())
        self.views = self.setup_views()

        csrf = CsrfProtect()
        csrf.init_app(self.app)

    def setup_views(self):
        views = {
            'general': MentorFinderViews(
                self.controller),
        }
        self.app.register_blueprint(views['general'])
        return views
