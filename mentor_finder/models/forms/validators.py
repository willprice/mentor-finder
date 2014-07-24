from wtforms import ValidationError


class DuplicateAccount(object):
    def __init__(self, faculty):
        self.faculty = faculty

    def __call__(self, form, field):
        email = field.data
        if self.faculty.get_mentor(email):
            raise ValidationError("That email address has already been registered")
