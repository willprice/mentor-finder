import flask.ext.testing
import mentor_finder


class FlaskTestCase(flask.ext.testing.TestCase):
    def create_app(self):
        self.finder = mentor_finder.MentorFinder()
        app = self.finder.app
        app.config['DEBUG'] = False
        app.config['TESTING'] = True
        app.config['WTF_CSRF_ENABLED'] = False
        app.secret_key = 'my_secret_key'
        return app
