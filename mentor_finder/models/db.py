# -*- coding: utf-8 -*-
from pymongo import MongoClient

from mentor_finder.models.converters import MentorDictionaryConverter
from mentor_finder.models.faculty import Faculty


class MongoDB(object):
    def __init__(self, uri, db_name):
        self.db = MongoClient(uri)[db_name]
        self.converter = MentorDictionaryConverter()
        self.mentors_collection = self.db['mentors']

    def get_mentor(self, email):
        mentor_data = self.mentors_collection.find_one({'email': email})
        if mentor_data:
            return self.converter.dictionary_to_mentor(mentor_data)
        return None

    def insert_mentor(self, mentor):
        mentor_data = self.converter.mentor_to_dictionary(mentor)
        return self.mentors_collection.insert(mentor_data)

    def update(self, mentor):
        stored_mentor_data = self.mentors_collection.find_one({'email': mentor.email})
        self.mentors_collection.update(
            {'_id': stored_mentor_data['_id']},
            {'$set': {
                'activated': mentor.activated
            }})

    def get_mentors(self):
        return map(
            MentorDictionaryConverter.dictionary_to_mentor,
            self.mentors_collection.find()
        )

