# -*- coding: utf-8 -*-
from mentor_finder.models.faculty_repository.abstract \
    import AbstractFacultyRespository
from mentor_finder.config import Config
from mentor_finder.models.faculty import Faculty
from mentor_finder.models.db import MongoDB


class PersistentFacultyRepository(AbstractFacultyRespository):
    def __init__(self, faculty=None, db=None):
        if not db:
            db = MongoDB(Config().config['db_uri'], 'mentor_finder')
        self.db = db
        if faculty:
            self._faculty = faculty
        else:
            self._faculty = self._load_faculty()

    def _load_faculty(self):
        mentors = self.db.get_mentors()
        return Faculty(mentors=mentors)

    def get_faculty(self):
        return self._faculty

    def insert_mentor(self, mentor):
        return self.db.insert_mentor(mentor)
