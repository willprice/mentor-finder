from .. import models
import datetime

_jasons_details = dict(
    first_name="Jason",
    last_name="Gorman",
    email="jasongorman@codemanship.com",
    county="Greater London",
    description="I am a London based software developer and trainer with 22 years of commercial experience",
    date_of_birth=datetime.date(1800,01,01)
)

def create_example_mentor(first_name=_jasons_details['first_name'],
                          last_name=_jasons_details['last_name'],
                          **kwargs):
    name = models.Name(first_name, last_name)
    return models.Mentor(name, dict(_jasons_details, **kwargs))
