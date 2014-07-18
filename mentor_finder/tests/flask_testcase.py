import flask.ext.testing
import mentor_finder


class FlaskTestCase(flask.ext.testing.TestCase):
    def create_app(self):
        app = mentor_finder.app
        app.config['TESTING'] = True
        return app
