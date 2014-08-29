# -*- coding: utf-8 -*-
from datetime import datetime
from mentor_finder.models.mentor_parser import MentorFieldParser
from mentor_finder.models.converters import MentorDictionaryConverter

_basic_mentor_details = dict(
    first_name="Jason",
    last_name="Gorman",
    email="jasongorman@codemanship.com",
    county="Greater London",
    description="I am a London based software developer and trainer with 22 years of commercial experience",
    date_of_birth="1900-01-01"
)

_jasons_details = dict(
    keywords="Programming,TDD,Refactoring",
    personal_site="parlezuml.com/blog",
    twitter_id="jasongorman",
    linkedin="uk.linkedin.com/in/jasongorman",
    **_basic_mentor_details
)


def create_minimal_example_mentor(**kwargs):
    return MentorFieldParser(dict(_basic_mentor_details, **kwargs)).get_mentor()


def create_example_mentor(**kwargs):
    mentor = MentorFieldParser(dict(_jasons_details, **kwargs)).get_mentor()
    try:
        if kwargs['activated']:
            mentor.activate()
    except KeyError:
        pass
    return mentor


EXAMPLE_MENTOR_DB_DATA = MentorDictionaryConverter() \
    .mentor_to_dictionary(create_example_mentor())

EXAMPLE_MENTOR_FORM_DATA = dict(
    password="apprentice",
    password_confirmation="apprentice",
    **_jasons_details
)


class FakeDatetime(datetime):
    def __new__(cls, *args, **kwargs):
        return datetime.__new__(*args, **kwargs)

