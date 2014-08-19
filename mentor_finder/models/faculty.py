from mentor_finder.models.errors import MentorAlreadyExistsError


class Faculty(object):
    def __init__(self):
        self.mentors = []

    def __iter__(self):
        return self.mentors.__iter__()

    def __str__(self):
        return str(map(str, self.mentors))

    def add(self, mentor):
        if mentor in self.mentors:
            raise MentorAlreadyExistsError
        self.mentors.append(mentor)

    def get_mentor(self, email):
        for mentor in self.mentors:
            if mentor.email == email:
                return mentor
        return None
