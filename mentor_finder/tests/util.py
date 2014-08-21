# -*- coding: utf-8 -*-
from datetime import datetime
import mentor_finder.models
from mentor_finder.models.mentor_parser import MentorFieldParser
EXAMPLE_MENTOR_FORM_DATA = dict(
    email="jasongorman@codemanship.com",
    password="apprentice",
    password_confirmation="apprentice",
    first_name="Jason",
    last_name="Gorman",
    county="Greater London",
    date_of_birth="1900-01-01",
    description="I am a London based software developer with 22 years commercial experience",
    keywords="tdd,xp",
    personal_site="parlezuml.com/blog",
    twitter_id="jasongorman",
)

_basic_mentor_details = dict(
    first_name="Jason",
    last_name="Gorman",
    email="jasongorman@codemanship.com",
    county="Greater London",
    description="I am a London based software developer and trainer with 22 years of commercial experience",
    date_of_birth=u"1900-01-01"
)

_jasons_details = dict(
    first_name="Jason",
    last_name="Gorman",
    email="jasongorman@codemanship.com",
    county="Greater London",
    description="I am a London based software developer and trainer with 22 years of commercial experience",
    date_of_birth=u"1900-01-01",
    keywords="Programming,TDD,Refactoring",
    personal_site="parlezuml.com/blog",
    twitter_id="jasongorman",
    linkedin="uk.linkedin.com/in/jasongorman"
)


def create_minimal_example_mentor(**kwargs):
    return MentorFieldParser(dict(_basic_mentor_details, **kwargs)).get_mentor()

def create_example_mentor(**kwargs):
    return MentorFieldParser(dict(_jasons_details,
                                 **kwargs)).get_mentor()


class FakeDatetime(datetime):
    def __new__(cls, *args, **kwargs):
        return datetime.__new__(*args, **kwargs)
