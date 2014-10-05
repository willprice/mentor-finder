# -*- coding: utf-8 -*-
import unittest
from mock import patch, MagicMock

from mentor_finder.config import Config
from mentor_finder.models.faculty_repository import PersistentFacultyRepository
from mentor_finder.tests.util import create_example_mentor


class TestPersistentFacultyRepository(unittest.TestCase):
    def setUp(self):
        self.db = MagicMock()
        self.repository = PersistentFacultyRepository(db=self.db)

    def test_adding_mentor_adds_to_db(self):
        mentor = create_example_mentor()

        self.repository.insert_mentor(mentor)

        self.db.insert_mentor.assert_called_once_with(mentor)

    @patch('mentor_finder.models.faculty_repository.persistent.Faculty')
    def test_loading_mentor_from_db(self, Faculty):
        mentors = self.db.get_mentors()
        self.repository._load_faculty()
        Faculty.assert_called_once_with(mentors=mentors)
