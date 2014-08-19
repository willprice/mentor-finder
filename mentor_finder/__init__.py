from flask_mail import Mail
from flask import Flask
from flask import url_for
from flask_wtf import CsrfProtect

import mentor_finder.views
from mentor_finder.web_controller import Controller


class MentorFinder(object):
    def __init__(self, secret_key="Super secret key"):
        self.app = Flask(__name__)
        self.app.secret_key = secret_key
        self.controller = Controller(self.app)
        self.app.register_blueprint(mentor_finder.views.mod)

finder = MentorFinder()
app = finder.app
controller = finder.controller


def serve_static_files():
    url_for('static', filename='css/main.css')
    url_for('static', filename='css/normalize.css')

if __name__ == '__main__':
    app.config.update(
        DEBUG=True,
        MAIL_SERVER='smtp.gmail.com',
        MAIL_PORT=587,
        MAIL_USE_TLS=True,
    )

    try:
        from mentor_finder.sensitive.passes import add_sensitive_information_to_app
        add_sensitive_information_to_app(app)
    except ImportError:
        print "Sensitive passes not found, continuing without, expect errors!"

    mail = Mail()
    csrf = CsrfProtect()

    csrf.init_app(app)
    mail.init_app(app)

    app.run()

if app.debug or app.testing:
    serve_static_files()
