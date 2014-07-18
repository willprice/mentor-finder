class Faculty(object):
    def __init__(self):
        self.mentors = []

    def __iter__(self):
        return self.mentors.__iter__()

    def add(self, mentor):
        self.mentors.append(mentor)

    def get_mentor(self, email):
        for mentor in self.mentors:
            if mentor.email == email:
                return mentor