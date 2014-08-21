# -*- coding: utf-8 -*-

from mentor_finder.models.faculty import Faculty
from mentor_finder.models.mentor_parser import MentorFieldParser
from mentor_finder.models.mailers import Mailer
from mentor_finder.util import flash_errors

def default_error_reporter(form):
    flash_errors(form)


class Controller(object):
    # Default objects are shared between invocations hence the use of
    #  `None` as a default and then setting the fields
    def __init__(self, app=None,
                 faculty=None,
                 activation_mailer=None,
                 error_reporter=default_error_reporter):
        if not faculty:
            faculty = Faculty()
        if not activation_mailer:
            activation_mailer = Mailer()
        self.activation_mailer = activation_mailer
        self.faculty = faculty
        self.error_reporter = error_reporter
        self.app = app

    def add_mentor(self, mentor_dict):
        mentor = MentorFieldParser(mentor_dict).get_mentor()
        if self.faculty.add(mentor):
            print "Adding mentor: " + mentor.email
            self.activation_mailer.send(mentor.email)
            return mentor
        else:
            return False


    def process_mentor_form(self, form, data, success_fn, fail_fn):
        if form.validate_on_submit():
                mentor = self.add_mentor(data)
                if mentor:
                    return success_fn(mentor)
                return fail_fn()
        else:
            self.error_reporter(form)
            return fail_fn()

    def activate_mentor(self, key):
        self.faculty.activate_mentor(key)

