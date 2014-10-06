# -*- coding: utf-8 -*-
import unittest
from pymongo import MongoClient
import datetime
from nose_parameterized import parameterized

from mentor_finder.models.db import MongoDB
from mentor_finder.tests.util import create_example_mentor, \
    EXAMPLE_MENTOR_DB_DATA, MentorDictionaryConverter
from mentor_finder.models.mentor import Mentor

class TestDb(unittest.TestCase):
    # Print really long diffs
    maxDiff = None

    @classmethod
    def setUpClass(cls):
        _client = MongoClient('localhost', 27017)
        _db_name = 'test_db'
        cls.db = _client[_db_name]
        cls.example_mentor = create_example_mentor()
        cls.db_wrapper = MongoDB("mongodb://localhost/", _db_name)

    def setUp(self):
        self.db.drop_collection('mentors')
        self.db['mentors'].insert(EXAMPLE_MENTOR_DB_DATA)

    def test_fetch_mentor(self):
        mentor = self.db_wrapper.get_mentor(self.example_mentor.email)
        expected_mentor = MentorDictionaryConverter.dictionary_to_mentor(EXAMPLE_MENTOR_DB_DATA)
        self.mentor_deep_equal(expected_mentor, mentor)

    def test_add_mentor(self):
        mentor_data = dict(
            first_name="Will",
            last_name="Price",
            email="will.price94@gmail.com",
            county="Hereford",
            description="I am a Hereford based software developer and trainer with "
                        "no years of commercial experience",
            date_of_birth=(1900, 02, 01),
            keywords=["Programming", "Python"],
            personal_site="willprice.org",
            twitter_id="will_price_94",
            linkedin="uk.linkedin.com/in/willprice",
            activated=True,
        )
        mentor = self.create_mentor(mentor_data)

        self.db_wrapper.save_mentor(mentor)

        fetched_mentor = self.db_wrapper.get_mentor(mentor.email)
        expected_mentor = MentorDictionaryConverter.dictionary_to_mentor(mentor_data)
        self.mentor_deep_equal(expected_mentor, fetched_mentor)

    def test_update_mentor(self):
        self.db_wrapper.save_mentor(self.example_mentor)
        updated_mentor_data = MentorDictionaryConverter.mentor_to_dictionary(self.example_mentor)
        updated_mentor_data.update(
            activated=True
        )
        print updated_mentor_data['activated']
        updated_mentor = self.create_mentor(updated_mentor_data)

        self.db_wrapper.update(updated_mentor)

        fetched_mentor = self.db_wrapper.get_mentor(updated_mentor.email)
        expected_mentor = MentorDictionaryConverter.dictionary_to_mentor(updated_mentor_data)
        self.mentor_deep_equal(expected_mentor, fetched_mentor)

    def test_load_faculty(self):
        faculty = self.db_wrapper.get_mentors()
        self.assertEqual(1, len(faculty))
        assert type(faculty[0]) == Mentor

    def create_mentor(self, mentor_data):
        diff = dict(
            keywords=",".join(mentor_data['keywords']),
            date_of_birth=datetime.date(*mentor_data['date_of_birth'])
        )
        copy = mentor_data.copy()
        copy.update(diff)
        return create_example_mentor(**copy)

    def mentor_deep_equal(self, expected_mentor, actual_mentor):
        self.assertIsNotNone(actual_mentor)
        actual_mentor_data = MentorDictionaryConverter.mentor_to_dictionary(
            actual_mentor
        )
        expected_mentor_data = MentorDictionaryConverter.mentor_to_dictionary(
            expected_mentor
        )
        self.assertEqual(expected_mentor_data, actual_mentor_data)

