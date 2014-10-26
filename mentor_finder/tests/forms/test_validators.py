# -*- coding: utf-8 -*-
import unittest
import datetime

from wtforms import Form, StringField, DateField

from mentor_finder.tests.testcases.flask_testcase import FlaskTestCase
from mentor_finder.views.forms.validators import DuplicateAccount, MinimumAge
from mentor_finder.models.faculty import Faculty
from mentor_finder.tests.util import create_example_mentor


class TestDuplicateAccountValidator(FlaskTestCase):
    def setUp(self):
        self.faculty = Faculty()
        self.mentor = create_example_mentor()
        self.faculty.add(self.mentor)

        class TestForm(Form):
            email = StringField(u'Email', [DuplicateAccount(self.faculty)])

        self.TestForm = TestForm


    def test_duplicate_account_raises_a_validation_error(self):
        form = self.TestForm(csrf_enabled=False)
        form.process(email=self.mentor.email)

        self.assertFalse(form.validate())

    def test_unknown_email_doesnt_raise_a_validation_error(self):
        form = self.TestForm(csrf_enabled=False)
        form.process(email=u"example@example.com")
        self.assertTrue(form.validate())

class TestMinimumAgeValidator(unittest.TestCase):
    def setUp(self):
        class TestForm(Form):
            date_of_birth = DateField(u'Date of birth', [MinimumAge(min=18)])

        self.TestForm = TestForm
        self.form = self.TestForm(csrf_enabled=False)

    def test_date_of_birth_less_than_18_years_ago_raises_a_validation_error(self):
        self.form.process(date_of_birth=datetime.date.today())
        self.assertFalse(self.form.validate())

    def test_date_of_birth_over_18_years_ago_doesnt_raise_a_validation_error(self):
        year = datetime.timedelta(days=365)
        eighteen_years = year * 18
        dob_over_eighteen = datetime.date.today() - eighteen_years
        self.form.process(date_of_birth=dob_over_eighteen)
        self.assertTrue(self.form.validate())
