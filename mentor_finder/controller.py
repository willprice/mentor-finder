from mentor_finder.models.faculty import Faculty
from mentor_finder.models.mentor import MentorFieldParser


class Controller(object):
    def __init__(self):
        self.faculty = Faculty()

    def add_mentor(self, mentor_dict):
        mentor_dict = mentor_dict.to_dict()
        self.faculty.add(MentorFieldParser(mentor_dict).create_mentor())