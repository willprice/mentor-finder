import datetime


class Mentor(object):
    def __init__(self, details):
        self._first_name = details['first_name']
        self._last_name = details['last_name']
        self._county = details['county']
        self._description = details['description']
        self._date_of_birth = details['date_of_birth']
        self._email = details['email']

    def __eq__(self, other):
        result = self.name == other.name
        result = result and self.county == other.county
        result = result and self.description == other.description
        result = result and self.date_of_birth == other.date_of_birth
        result = result and self.email == other.email
        return result

    @property
    def name(self):
        return self._first_name + " " + self._last_name

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

