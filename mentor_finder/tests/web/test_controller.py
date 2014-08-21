# -*- coding: utf-8 -*-
import unittest

from mock import Mock
from mentor_finder.models.message import ActivationMessage

import mentor_finder.web_controller
from mentor_finder.tests.util import EXAMPLE_MENTOR_FORM_DATA


class TestController(unittest.TestCase):
    def setUp(self):
        self.controller = mentor_finder.web_controller.Controller()

    def test_activating_mentor_delegates_to_faculty(self):
        token = "EXAMPLE_TOKEN"
        faculty = Mock()

        controller = mentor_finder.web_controller.Controller(
            faculty=faculty)
        controller.activate_mentor(token)

        faculty.activate_mentor.assert_called_with(token)

    def test_adding_mentor_sends_activation_email(self):
        mailer = Mock()
        controller = mentor_finder.web_controller.Controller(
            activation_mailer=mailer
        )
        controller.add_mentor(EXAMPLE_MENTOR_FORM_DATA)
        mailer.send.assert_called_once_with(
            EXAMPLE_MENTOR_FORM_DATA['email']
        )

