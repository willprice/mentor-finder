# -*- coding: utf-8 -*-
import unittest
from mock import patch, Mock

from mentor_finder.models.mail.message import ActivationMessage
from mentor_finder.tests.util import create_example_mentor
from mentor_finder.config import Config

class TestActivationMessage(unittest.TestCase):
    @patch('mentor_finder.models.mail.message.Config')
    def test_activation_message_contains_verifcation_url(self, mock_Config):
       mentor = create_example_mentor()
       config = Config()
       mock_Config.return_value = config
       url = "www.example.com"
       config.config['url'] = url
       config.config['secret_key'] = "so secret"

       message = ActivationMessage(mentor)

       self.assertIn(url + "/users/activate/", message.plain)
