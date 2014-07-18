import mentor_finder.models
import datetime
from mentor_finder.models.mentor import MentorFieldParser

_basic_mentor_details = dict(
    first_name="Jason",
    last_name="Gorman",
    email="jasongorman@codemanship.com",
    county="Greater London",
    description="I am a London based software developer and trainer with 22 years of commercial experience",
    date_of_birth=datetime.date(1800,01,01),
)

_jasons_details = dict(
    first_name="Jason",
    last_name="Gorman",
    email="jasongorman@codemanship.com",
    county="Greater London",
    description="I am a London based software developer and trainer with 22 years of commercial experience",
    date_of_birth=datetime.date(1800,01,01),
    keywords="programming,tdd",
    personal_site="parlezuml.com/blog",
    twitter_id="jasongorman"
)


def create_minimal_example_mentor(**kwargs):
    return MentorFieldParser(dict(_basic_mentor_details, **kwargs)).create_mentor()

def create_example_mentor(**kwargs):
    return MentorFieldParser(dict(_jasons_details, **kwargs)).create_mentor()
