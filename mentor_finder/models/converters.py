# -*- coding: utf-8 -*-
import datetime
from bson import BSON
from mentor_finder.models.mentor import Mentor
from mentor_finder.models.name import Name


class MentorDictionaryConverter(object):
    """ Converts a mentor into a dictionary and vica versa keeping it in a
    format that is suitable for adding to a collection in mongodb.
    """
    @staticmethod
    def dictionary_to_mentor(mentor_data):
        mentor = Mentor(name=Name(mentor_data['first_name'],
                                mentor_data['last_name']),
                        password=mentor_data['password'],
                        email=mentor_data['email'],
                        county=mentor_data['county'],
                        description=mentor_data['description'],
                        date_of_birth=datetime.date(*mentor_data['date_of_birth']),
                        keywords=mentor_data['keywords'],
                        personal_site=mentor_data['personal_site'],
                        twitter_id=mentor_data['twitter_id'],
                        linkedin=mentor_data['linkedin'],
                        )
        try:
            activated = mentor_data['activated']
            if activated:
                mentor.activate()
        except KeyError:
            pass
        return mentor


    @staticmethod
    def mentor_to_dictionary(mentor):
        mentor_data = dict(
            first_name=str(mentor.name.first),
            last_name=str(mentor.name.second),
            password=str(mentor.password),
            email=str(mentor.email),
            county=str(mentor.county),
            description=str(mentor.description),
            date_of_birth=mentor.date_of_birth.timetuple()[0:3],
            keywords=map(str, mentor.keywords),
            personal_site=str(mentor.personal_site),
            twitter_id=str(mentor.twitter_id),
            linkedin=str(mentor.linkedin),
            activated=mentor.activated
        )
        return mentor_data
