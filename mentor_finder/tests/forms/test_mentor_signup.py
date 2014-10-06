# -*- coding: utf-8 -*-
from nose_parameterized import parameterized

from wtforms_test import FormTestCase
from mentor_finder.views.forms.mentor_signup import mentor_signup_form_factory
from mentor_finder.views.forms.validators import DuplicateAccount
from mentor_finder.models.faculty import Faculty


class TestMentorSignupForm(FormTestCase):
    faculty = Faculty()
    form_class = mentor_signup_form_factory(faculty, test=True)

    @parameterized.expand([
        ['first_name'],
        ['last_name'],
        ['date_of_birth'],
        ['county'],
        ['email'],
        ['password'],
        ['password_confirmation'],
        ['description']
    ])
    def test_field_is_required(self, field):
        self.assert_required(field)

    @parameterized.expand([
        ['keywords'],
        ['personal_site'],
        ['twitter_id'],
        ['linkedin'],
        ['github_id'],
    ])
    def test_field_is_optional(self, field):
        self.assert_optional(field)

    @parameterized.expand([
        ["John*"],
        ["Tim*"],
        ["John$"]
    ])
    def test_first_name_doesnt_accept_nonalphabetic_names(self, invalid_first_name):
        self.assert_invalid({'first_name': invalid_first_name}, 'first_name')

    def test_first_name_accepts_alphabetic_names(self):
        self.assert_valid({'first_name': "John"})

    @parameterized.expand([
        ["Johnson*"],
        ["Timson*"],
        ["Johnson$"]
    ])
    def test_first_name_doesnt_accept_nonalphabetic_names(self, invalid_last_name):
        self.assert_invalid({'last_name': invalid_last_name}, 'last_name')

    def test_first_name_accepts_alphabetic_names(self):
        self.assert_valid({'last_name': "Johnson"})

    def test_password_confirmation_has_to_match_password(self):
        self.assert_invalid({'password': 'apprentice',
                             'password_confirmation': 'Apprentice'}, 'password')

    def test_checks_for_duplicate_accounts(self):
        self.assert_has_validator('email', DuplicateAccount)

    def test_password_5_characters_long_is_not_accepted(self):
        self.assert_invalid({'password': 'xxxxx',
                             'password_confirmation': 'xxxxx'}, 'password')

    def test_password_6_characters_long_is_valid(self):
        self.assert_valid({'password': 'xxxxxx',
                           'password_confirmation': 'xxxxxx'})
