# -*- coding: utf-8 -*-
from mentor_finder import Config


class AbstractFacultyRespository(object):
    """ All methods must be implemented to be a faculty repository
        attributes:
        _faculty
    """
    def __init__(self, faculty=None):
        pass

    def get_faculty(self):
        pass

    def insert_mentor(self, mentor):
        pass
