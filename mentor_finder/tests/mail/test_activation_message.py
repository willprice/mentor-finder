# -*- coding: utf-8 -*-
import unittest
from itsdangerous import URLSafeSerializer
from marrow.mailer.address import Address
from mock import Mock
from nose_parameterized import parameterized
from mentor_finder.models.message import ActivationMessage
from mentor_finder.tests.util import create_example_mentor
import mentor_finder.web_controller


example_mentors = [
    [create_example_mentor()],
    [create_example_mentor(email="jo@jo.com")]
]

class TestActivationMessage(unittest.TestCase):
    secret_key = "secret_key"

    def setUp(self):
        app = Mock()
        app.secret_key = self.secret_key

    @parameterized.expand(example_mentors)
    def test_message_contains_email_address_of_mentor(self, mentor):
        activation_email = ActivationMessage(mentor, self.secret_key)
        self.assertIn(Address(mentor.email), activation_email.to)


    @parameterized.expand(example_mentors)
    def test_message_contains_activation_token(self, mentor):
        serializer = URLSafeSerializer(self.secret_key)
        expected_token = serializer.dumps(mentor.email)
        activation_email = ActivationMessage(mentor, self.secret_key)
        self.assertIn(expected_token, activation_email.plain)

    @parameterized.expand(example_mentors)
    def test_message_contains_users_first_name(self, mentor):
        activation_email = ActivationMessage(mentor, self.secret_key)
        self.assertIn(mentor.name.first, activation_email.plain)
