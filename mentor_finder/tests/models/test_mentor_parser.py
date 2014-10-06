# -*- coding: utf-8 -*-
import unittest

from mentor_finder.hash import Hash
from mentor_finder.models.mentor_parser import MentorFieldParser
from mentor_finder.tests.util import create_example_mentor_form_data


class TestMentorFieldParser(unittest.TestCase):
    def test_hashing_password(self):
        password = "test_password"
        parser = MentorFieldParser(create_example_mentor_form_data(
            password=password)
        )
        mentor = parser.get_mentor()
        hashed_password = Hash().hash(password)
        self.assertEqual(hashed_password, mentor.password)
