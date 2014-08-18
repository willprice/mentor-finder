import flask.ext.testing
import mentor_finder


class FlaskTestCase(flask.ext.testing.TestCase):
    def create_app(self):
        app = mentor_finder.app


        app.debug = True
        app.config['TESTING'] = True
        app.config['WTF_CSRF_ENABLED'] = False
        app.secret_key = 'my_secret_key'
        return app
