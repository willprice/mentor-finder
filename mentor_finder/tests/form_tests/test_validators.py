from mentor_finder.tests.flask_testcase import FlaskTestCase
from mentor_finder.models.forms.validators import DuplicateAccount
from mentor_finder.models.faculty import Faculty
from mentor_finder.tests.utilities import create_example_mentor

from wtforms import ValidationError, Form, StringField



class TestValidators(FlaskTestCase):

    def setUp(self):
        self.faculty = Faculty()
        self.mentor = create_example_mentor()
        self.faculty.add(self.mentor)

        class TestForm(Form):
            email = StringField(u'Email field', [DuplicateAccount(self.faculty)])

        self.TestForm = TestForm


    def test_duplicate_account_raises_a_validation_error(self):
        form = self.TestForm(csrf_enabled=False)
        form.process(email=self.mentor.email)

        self.assertFalse(form.validate())

    def test_unknown_email_doesnt_raise_a_validation_error(self):
        form = self.TestForm(csrf_enabled=False)
        form.process(email="example@example.com")
        self.assertTrue(form.validate())

