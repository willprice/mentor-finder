import datetime
import dateutil.parser
from mentor_finder.models.name import Name


class MentorFieldParser(object):
    def __init__(self, fields):
        self.fields = fields
        self.optional_fields = dict()
        county, date_of_birth, description, email, name = self.parse_mandatory_fields()
        self.parse_optional_fields()
        self.mentor = Mentor(name, county, description, date_of_birth, email, **self.optional_fields)

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


class Mentor(object):
    def __init__(self, name, county, description, date_of_birth, email,
                 personal_site=None, twitter_id=None, keywords=None,
                 linkedin=None, github_id=None):
        self.activated = False
        self._name = name
        self._county = county
        self._description = description
        self._date_of_birth = date_of_birth
        self._email = email
        self._personal_site = personal_site
        self._twitter_id = twitter_id
        self._keywords = keywords
        self._linkedin_id = linkedin
        self._github_id = github_id


    def __ne__(self, other):
        return not self.__eq__(other)

    def __eq__(self, other):
        if type(other) == Mentor:
            return self.email == other.email
        return False

    @property
    def name(self):
        return self._name

    @property
    def email(self):
        return self._email

    @property
    def county(self):
        return self._county

    @property
    def description(self):
        return self._description

    @property
    def date_of_birth(self):
        return self._date_of_birth

    @property
    def keywords(self):
        return self._keywords

    @property
    def personal_site(self):
        return self._personal_site

    @property
    def twitter_id(self):
        return  self._twitter_id

    @property
    def linkedin(self):
        return self._linkedin_id

    @property
    def github_id(self):
        return self._github_id
