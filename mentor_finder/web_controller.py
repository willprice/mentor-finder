from mentor_finder.models.errors import MentorAlreadyExistsError
from mentor_finder.models.faculty import Faculty
from mentor_finder.models.mentor import MentorFieldParser
from mentor_finder.web import flash_errors

class Controller(object):

    def __init__(self, app, error_reporter=lambda form: flash_errors(form)):
        self.faculty = Faculty()
        self.app = app
        self.error_reporter = error_reporter

    def add_mentor(self, mentor_dict):
        mentor = MentorFieldParser(mentor_dict).get_mentor()
        try:
            self.faculty.add(mentor)
            added = True
        except MentorAlreadyExistsError:
            added = False
        return added, mentor

    def process_mentor_form(self, form, data, success_fn, fail_fn):
        if form.validate_on_submit():
                added, mentor = self.add_mentor(data)
                if added:
                    return success_fn(mentor)
                else:
                    return fail_fn()
        else:
            self.error_reporter(form)
            return fail_fn()

