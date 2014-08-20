# -*- coding: utf-8 -*-
import unittest
from mock import Mock

from mentor_finder import MentorFinder


class TestMentorFinder(unittest.TestCase):
    def test_activating_existing_unactivated_mentor_actives_mentor(self):
        finder = MentorFinder()
        finder.controller.activate_mentor = Mock()
        key = "EXAMPLE_URL_SAFE_KEY"
        finder.activate_mentor(key)
        finder.controller.activate_mentor.assert_any_call()
