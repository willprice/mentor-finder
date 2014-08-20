# -*- coding: utf-8 -*-
from mentor_finder.models.errors import MentorAlreadyExistsError
from mentor_finder.models.faculty import Faculty
from mentor_finder.models.mentor_parser import MentorFieldParser
from mentor_finder.web import flash_errors

def default_error_reporter(form):
    flash_errors(form)

class Controller(object):
    def __init__(self, app, error_reporter=default_error_reporter):
        self.faculty = Faculty()
        self.app = app
        self.error_reporter = error_reporter

    def add_mentor(self, mentor_dict):
        mentor = MentorFieldParser(mentor_dict).get_mentor()
        try:
            self.faculty.add(mentor)
            return mentor
        except MentorAlreadyExistsError:
            return None

    def process_mentor_form(self, form, data, success_fn, fail_fn):
        if form.validate_on_submit():
                mentor = self.add_mentor(data)
                if mentor:
                    return success_fn(mentor)
                return fail_fn()
        else:
            self.error_reporter(form)
            return fail_fn()
