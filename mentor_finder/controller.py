from mentor_finder.models.errors import MentorAlreadyExistsError
from mentor_finder.models.faculty import Faculty
from mentor_finder.models.mentor import MentorFieldParser


class Controller(object):
    def __init__(self):
        self.faculty = Faculty()

    def add_mentor(self, mentor_dict):
        mentor = MentorFieldParser(mentor_dict).get_mentor()
        self.faculty.add(mentor)
        return mentor
