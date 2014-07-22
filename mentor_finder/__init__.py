from flask import Flask
from flask import url_for


from mentor_finder.controller import Controller

app = Flask(__name__)
controller = Controller()

import mentor_finder.views
app.register_blueprint(mentor_finder.views.mod)

def serve_static_files():
    url_for('static', filename='css/main.css')
    url_for('static', filename='css/normalize.css')

if __name__ == '__main__':
    app.debug = True
    app.secret_key = "A0Zr98j/3yX R~XHH!jmN]LWX/,?RT"
    app.run()
    if app.debug:
        serve_static_files()
