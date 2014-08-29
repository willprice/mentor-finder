# -*- coding: utf-8 -*-
import itsdangerous


class Faculty(object):
    def __init__(self, mentors=None):
        if not mentors:
            self.mentors = []
        else:
            self.mentors = mentors

    def __iter__(self):
        return self.mentors.__iter__()

    def __str__(self):
        return str(map(str, self.mentors))

    def add(self, mentor):
        if mentor in self.mentors:
            return False
        self.mentors.append(mentor)
        return True

    def get_mentor(self, email):
        for mentor in self.mentors:
            if mentor.email == email:
                return mentor
        return None

    def activate_mentor(self, token, key):
        serializer = itsdangerous.URLSafeSerializer(key)
        email = serializer.loads(token)
        mentor = self.get_mentor(email)
        mentor.activate()

    def exists(self, mentor):
        return mentor in self.mentors
