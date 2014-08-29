# -*- coding: utf-8 -*-
import unittest

from mock import Mock, patch

from mentor_finder.controller import Controller
from mentor_finder.models.mail.mailers import StubMailer
from mentor_finder.tests.util import EXAMPLE_MENTOR_FORM_DATA


class TestController(unittest.TestCase):
    def setUp(self):
        self.controller = Controller()


    @patch('mentor_finder.controller.ActivationMessage')
    def test_adding_mentor_sends_activation_email(self, ActivationMessage):
        message = Mock()
        ActivationMessage.return_value=message
        mailer = Mock()
        controller = Controller(mailer=mailer)
        controller.add_mentor(EXAMPLE_MENTOR_FORM_DATA)
        mailer.send.assert_called_once_with(message)

    def test_adding_mentor_triggers_save_to_mentor_repository(self):
        repository = Mock()
        controller = Controller(repository=repository,
                                mailer=StubMailer())
        mentor = controller.add_mentor(EXAMPLE_MENTOR_FORM_DATA)
        repository.insert_mentor.assert_called_once_with(mentor)
