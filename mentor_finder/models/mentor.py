import datetime
from mentor_finder.models.name import Name


class MentorFieldParser(object):
    def __init__(self, fields):
        self.fields = fields
        self.optional_fields = dict()

    def create_mentor(self):
        county, date_of_birth, description, email, name = self.parse_mandatory_fields()
        self.parse_optional_fields()
        return Mentor(name, county, description, date_of_birth,
                      email, **self.optional_fields)

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
            date_of_birth = fields['date_of_birth']
        except KeyError:
            date_of_birth = datetime.date(int(fields['dob_year']),
                                          int(fields['dob_month']),
                                          int(fields['dob_day']))
        return date_of_birth

    def parse_optional_fields(self):
        self.parse_optional_keywords()
        self.parse_optional_field('twitter_id')
        self.parse_optional_field('personal_site')

    def parse_optional_field(self, field):
        try:
            self.optional_fields[field] = self.fields[field]
        except KeyError:
            pass

    def parse_optional_keywords(self):
        try:
            self.optional_fields['keywords'] = self.fields['keywords'].split(",")
        except KeyError:
            pass


class Mentor(object):
    def __init__(self, name, county, description, date_of_birth, email,
                 personal_site=None,
                 twitter_id=None,
                 keywords=None):
        self._name = name
        self._county = county
        self._description = description
        self._date_of_birth = date_of_birth
        self._email = email
        self._personal_site = personal_site
        self._twitter_id = twitter_id
        self._keywords = keywords


    def __ne__(self, other):
        return not self.__eq__(other)

    def __eq__(self, other):
        return self.email == other.email

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
    def linkedin_id(self):
        return "jasongorman"