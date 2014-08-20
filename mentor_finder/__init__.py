# -*- coding: utf-8 -*-
from flask import Flask
from flask_wtf import CsrfProtect

import mentor_finder.views
from mentor_finder.views.mentor_finder_views import MentorFinderViews
from mentor_finder.web_controller import Controller


class MentorFinder(object):
    def __init__(self, secret_key="Super secret key"):
        self.app = Flask(__name__)
        self.app.secret_key = secret_key

        self.controller = Controller(self.app)
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
