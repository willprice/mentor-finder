from flask_mail import Mail
from flask import Flask
from flask import url_for
from flask_wtf import CsrfProtect

from mentor_finder.web_controller import Controller


app = Flask(__name__)
app.secret_key = "A0Zr98j/3yX R~XHH!jmN]LWX/,?RT"

controller = Controller(app)
mail = Mail()
csrf = CsrfProtect()

import mentor_finder.views
app.register_blueprint(mentor_finder.views.mod)

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

    csrf.init_app(app)
    mail.init_app(app)

    app.run()

    if app.debug:
        serve_static_files()
