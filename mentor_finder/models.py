import datetime


class Faculty(object):
    def __init__(self):
        self.mentors = []

    def __iter__(self):
        return self.mentors.__iter__()

    def add(self, mentor):
        self.mentors.append(mentor)

    def get_mentor(self, email):
        for mentor in self.mentors:
            if mentor.email == email:
                return mentor


class Name(object):
    def __init__(self, first_name, second_name):
        self._first_name = first_name
        self._second_name = second_name

    def __eq__(self, other):
        return self._first_name == other._first_name and \
               self._second_name == other._second_name

    def __str__(self):
        return self._first_name + " " + self._second_name


class Mentor(object):
    @classmethod
    def create(cls, fields):
        name = Name(fields['first_name'],
                    fields['last_name'])
        county = fields['county']
        try:
            date_of_birth = fields['date_of_birth']
        except KeyError:
            date_of_birth = datetime.date(int(fields['dob_year']),
                                          int(fields['dob_month']),
                                          int(fields['dob_day']))
        description = fields['description']
        email = fields['email']
        optional = dict()
        try:
            optional['keywords'] = fields['keywords'].split(",")
        except KeyError:
            pass
        try:
            optional['personal_site'] = fields['personal_site']
        except KeyError:
            pass
        try:
            optional['twitter_id'] = fields['twitter_id']
        except KeyError:
            pass

        return cls(name, county, description, date_of_birth,
                   email, **optional)

    def add_optional_field(self, optional, field_name):
        try:
            self.__dict__['_' + field_name] = optional[field_name]
        except KeyError:
            pass

    def add_optional_fields(self, optional):
        self.add_optional_field(optional, 'personal_site')
        self.add_optional_field(optional, 'twitter_id')
        self.add_optional_field(optional, 'keywords')

    def __init__(self, name, county, description, date_of_birth,
                 email, **optional):
        self._name = name
        self._county = county
        self._description = description
        self._date_of_birth = date_of_birth
        self._email = email

        self.add_optional_fields(optional)

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
