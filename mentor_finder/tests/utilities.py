import mentor_finder.models
import datetime

_jasons_details = dict(
    first_name="Jason",
    last_name="Gorman",
    email="jasongorman@codemanship.com",
    county="Greater London",
    description="I am a London based software developer and trainer with 22 years of commercial experience",
    date_of_birth=datetime.date(1800,01,01)
)


def create_example_mentor(**kwargs):
    return mentor_finder.models.Mentor.create(dict(_jasons_details, **kwargs))
