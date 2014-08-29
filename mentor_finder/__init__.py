# -*- coding: utf-8 -*-
from flask import Flask
from flask_wtf import CsrfProtect

from mentor_finder.config import Config
import mentor_finder.views
from mentor_finder.views.mentor_finder_views import MentorFinderViews
from mentor_finder.controller import Controller
from mentor_finder.models.mail.mailers import StubMailer, Mailer


class MentorFinder(object):
    def __init__(self, test=False):
        self.config = Config().config
        self.app = Flask(__name__,
                         static_folder='static/dist',
                         static_url_path='/static')
        self.app.secret_key = self.config['secret_key']

        if test:
            self.app.config['TESTING'] = True
            mailer_cls = StubMailer
        else:
            mailer_cls = Mailer
            csrf = CsrfProtect()
            csrf.init_app(self.app)

        self.controller = Controller(mailer=mailer_cls())
        self.views = self.setup_views()

    def setup_views(self):
        views = {
            'general': MentorFinderViews(
                self.controller),
        }
        self.app.register_blueprint(views['general'])
        return views
