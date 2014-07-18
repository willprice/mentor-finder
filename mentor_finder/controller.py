from mentor_finder.models import Faculty, Mentor


class Controller(object):
    def __init__(self):
        self.faculty = Faculty()

    def add_mentor(self, mentor_dict):
        mentor_dict = mentor_dict.to_dict()
        self.faculty.add(Mentor.create(mentor_dict))