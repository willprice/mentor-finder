# -*- coding: utf-8 -*-
import unittest
from mock import patch, Mock

from mentor_finder.config import Config
from mentor_finder.models.mailers import Mailer
from mentor_finder.models.message import Message


class TestMailer(unittest.TestCase):
    @patch('mentor_finder.models.mailers.MarrowMailer')
    def test_send(self, marrow_mailer):
        marrow_mailer_instance = Mock()
        marrow_mailer.return_value = marrow_mailer_instance
        address = "example@example.com"
        message = Message(to=address)
        mailer = Mailer()

        mailer.send(message)

        marrow_mailer_instance.start.assert_called_once_with()
        marrow_mailer_instance.send.assert_called_once_with(message)
        marrow_mailer_instance.stop.assert_called_once_with()

    def test_loads_configuration(self):
        config = Config().config
        mailer = Mailer()
        self.assertEqual(config['mail']['username'], mailer.config['username'])

