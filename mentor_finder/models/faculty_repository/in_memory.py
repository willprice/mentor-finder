# -*- coding: utf-8 -*-
from mentor_finder.models.faculty import Faculty
from mentor_finder.models.faculty_repository.abstract \
    import AbstractFacultyRespository


class FacultyRepository(AbstractFacultyRespository):
    def __init__(self, faculty=Faculty()):
        self._faculty = faculty

    def get_faculty(self):
        return self._faculty

    def insert_mentor(self, mentor):
        return self._faculty.add(mentor)


