# -*- coding: utf-8 -*-
import unittest
from mentor_finder.models.errors import MentorAlreadyExistsError
from mentor_finder.models.faculty import Faculty
from mentor_finder.tests.util import create_example_mentor
import itsdangerous


class TestFaculty(unittest.TestCase):
    def setUp(self):
        self.faculty = Faculty()
        self.mentor = create_example_mentor()
        self.faculty.add(self.mentor)

    def test_existing_mentor_exists_in_faculty(self):
        self.assertTrue(self.faculty.exists(self.mentor))

    def test_mentors_with_same_credentials_but_email_can_coexist(self):
        another_mentor = create_example_mentor(email="willprice94@gmail.com")
        self.faculty.add(another_mentor)

    def test_activate_mentor(self):
        self.faculty.activate_mentor(self.mentor.email)
        self.assertTrue(self.mentor.activated)
