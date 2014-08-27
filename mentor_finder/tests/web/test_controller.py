# -*- coding: utf-8 -*-
import unittest

from mock import Mock, patch

from mentor_finder.controller import Controller
from mentor_finder.tests.util import EXAMPLE_MENTOR_FORM_DATA
from mentor_finder.config import Config


class TestController(unittest.TestCase):
    def setUp(self):
        self.controller = Controller()

    def test_activating_mentor_delegates_to_faculty(self):
        token = "EXAMPLE_TOKEN"
        faculty = Mock()

        controller = Controller(faculty=faculty)
        controller.activate_mentor(token)

        faculty.activate_mentor.assert_called_with(token,
                                                   Config().config['secret_key'])

    @patch('mentor_finder.controller.ActivationMessage')
    def test_adding_mentor_sends_activation_email(self, ActivationMessage):
        message = Mock()
        ActivationMessage.return_value=message
        mailer = Mock()
        controller = Controller(
            mailer=mailer
        )
        mentor = controller.add_mentor(EXAMPLE_MENTOR_FORM_DATA)
        mailer.send.assert_called_once_with(
            message
        )

