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
    def __init__(self, name, details):
        self._name = name
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

