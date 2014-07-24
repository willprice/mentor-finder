from flask_mail import Mail, Message
from flask import Flask
from flask import url_for
from flask_wtf import CsrfProtect


from mentor_finder.controller import Controller
from mentor_finder.passes import add_sensitive_information_to_app

app = Flask(__name__)
app.secret_key = "A0Zr98j/3yX R~XHH!jmN]LWX/,?RT"

controller = Controller()
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

    add_sensitive_information_to_app(app)

    csrf.init_app(app)
    mail.init_app(app)

    app.run()

    if app.debug:
        serve_static_files()
