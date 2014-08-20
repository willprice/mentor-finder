# -*- coding: utf-8 -*-
import unittest
from mentor_finder.models.errors import MentorAlreadyExistsError
from mentor_finder.models.faculty import Faculty
from utilities import create_example_mentor


class TestFaculty(unittest.TestCase):
    def setUp(self):
        self.faculty = Faculty()
        self.mentor = create_example_mentor()

    def test_adding_already_present_mentor_throws_exception(self):
        self.faculty.add(self.mentor)
        self.assertRaises(MentorAlreadyExistsError, lambda : self.faculty.add(self.mentor))

    def test_mentors_with_same_credentials_but_email_can_coexist(self):
        another_mentor = create_example_mentor(email="willprice94@gmail.com")
        self.faculty.add(self.mentor)
        self.faculty.add(another_mentor)
