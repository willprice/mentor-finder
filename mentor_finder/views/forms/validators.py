# -*- coding: utf-8 -*-
from wtforms import ValidationError
import datetime
import dateutil


class DuplicateAccount(object):
    def __init__(self, faculty):
        self.faculty = faculty

    def __call__(self, form, field):
        email = field.data
        if self.faculty.get_mentor(email):
            raise ValidationError("Sorry, but that email address has already been registered")

class MinimumAge(object):
    def __init__(self, min=18):
        self.min_age = min
        pass

    def __call__(self, form, field):
        dob = field.data #dateutil.parser.parse(field.data)
        age = datetime.date.today() - dob
        if age < datetime.timedelta(days=365*self.min_age):
            raise ValidationError("Sorry, but you must be at least {} years old to be a mentor".format(self.min_age))
