# -*- coding: utf-8 -*-

from mentor_finder.config import Config
from mentor_finder.email_deserializer import EmailDeserializer
from mentor_finder.models.faculty_repository import PersistentFacultyRepository
from mentor_finder.models.mentor_parser import MentorFieldParser
from mentor_finder.models.mail.mailers import Mailer
from mentor_finder.models.mail.message import ActivationMessage

from mentor_finder.util import flash_errors

def default_error_reporter(form):
    flash_errors(form)


class Controller(object):
    # Default objects are shared between invocations hence the use of
    #  `None` as a default and then setting the fields
    def __init__(self,
                 mailer=None,
                 error_reporter=default_error_reporter,
                 repository=PersistentFacultyRepository()):
        self.faculty_repository = repository
        if not mailer:
            mailer = Mailer()
        self.mailer = mailer
        self.error_reporter = error_reporter


    def add_mentor(self, mentor_dict):
        mentor = MentorFieldParser(mentor_dict).get_mentor()
        if self.faculty_repository.insert_mentor(mentor):
            self.mailer.send_activation_message_to_mentor(mentor)
            return mentor
        else:
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

    def activate_mentor(self, token):
        deserializer = EmailDeserializer()
        email = deserializer.deserialize_token_to_email(Config().config['secret_key'],
                                                        token)
        self.faculty_repository.activate_mentor(email)

    @property
    def faculty(self):
        return self.faculty_repository.get_faculty()
