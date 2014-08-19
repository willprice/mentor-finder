from datetime import datetime
import dateutil.parser

from mentor_finder.models.mentor import Mentor
from mentor_finder.models.name import Name


class MentorFieldParser(object):
    def __init__(self, fields):
        self.fields = fields
        self.optional_fields = dict()
        county, date_of_birth, description, email, name = self.parse_mandatory_fields()
        self.parse_optional_fields()
        self.mentor = Mentor(name, county, description, date_of_birth,
                             email,
                             signup_date=datetime.now(),
                             **self.optional_fields)

    def get_mentor(self):
        return self.mentor

    def parse_mandatory_fields(self):
        name = Name(self.fields['first_name'],
                    self.fields['last_name'])
        county = self.fields['county']
        date_of_birth = self.parse_date_of_birth(self.fields)
        description = self.fields['description']
        email = self.fields['email']
        return county, date_of_birth, description, email, name

    def parse_date_of_birth(self, fields):
        try:
            date_of_birth = dateutil.parser.parse(fields['date_of_birth'])
        except AttributeError:
            date_of_birth = fields['date_of_birth']
        return date_of_birth

    def parse_optional_fields(self):
        self.parse_keywords()
        self.parse_optional_field('twitter_id')
        self.parse_optional_field('personal_site')
        self.parse_optional_field('linkedin')
        self.parse_optional_field('github_id')

    def parse_optional_field(self, field):
        try:
            self.optional_fields[field] = self.fields[field]
        except KeyError:
            pass

    def parse_keywords(self):
        try:
            split_keywords = self.fields['keywords'].split(",")
            self.optional_fields['keywords'] = split_keywords if split_keywords != [''] else []
        except KeyError:
            pass
