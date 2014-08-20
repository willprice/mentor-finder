# -*- coding: utf-8 -*-
class Mentor(object):
    def __init__(self, name, county, description, date_of_birth, email,
                 personal_site=None, twitter_id=None, keywords=None,
                 linkedin=None, github_id=None, signup_date=None):
        self.signup_date = signup_date
        self.activated = False
        self.name = name
        self.county = county
        self.description = description
        self.date_of_birth = date_of_birth
        self.email = email
        self.personal_site = personal_site
        self.twitter_id = twitter_id
        self.keywords = keywords
        self.linkedin = linkedin
        self.github_id = github_id


    def __str__(self):
        return self.email

    def __ne__(self, other):
        return not self.__eq__(other)

    def __eq__(self, other):
        if type(other) == Mentor:
            return self.email == other.email
        return False
