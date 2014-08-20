# -*- coding: utf-8 -*-
import unittest
from mock import Mock

from mentor_finder import MentorFinder


class TestController(unittest.TestCase):
    @unittest.skip('Need to fix')
    def test_activating_existing_unactivated_mentor_actives_mentor(self):
        finder = MentorFinder()
        controller = finder.controller
        controller.activate_mentor = Mock()
        key = "EXAMPLE_URL_SAFE_KEY"
        controller.activate_mentor.assert_any_call()
