# -*- coding: utf-8 -*-
from datetime import datetime
from mentor_finder.hash import Hash
from mentor_finder.models.mentor_parser import MentorFieldParser
from mentor_finder.models.converters import MentorDictionaryConverter

_basic_mentor_details = dict(
    first_name="Jason",
    last_name="Gorman",
    password=Hash().hash("DEFAULT_PASSWORD"),
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
        if kwargs['not_activated']:
            pass
        else:
            mentor.activate()
    except KeyError:
            mentor.activate()
    return mentor


EXAMPLE_MENTOR_DB_DATA = MentorDictionaryConverter().mentor_to_dictionary(create_example_mentor())

EXAMPLE_MENTOR_FORM_DATA = _jasons_details

def create_example_mentor_form_data(**kwargs):
    mentor_form_data = EXAMPLE_MENTOR_FORM_DATA.copy()
    mentor_form_data.update(kwargs)
    return mentor_form_data


class FakeDatetime(datetime):
    def __new__(cls, *args, **kwargs):
        return datetime.__new__(*args, **kwargs)

