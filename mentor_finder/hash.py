# -*- coding: utf-8 -*-
import hashlib
from mentor_finder import Config

class Hash(object):
    def hash(self, string, number_of_rounds=100):
        hashed_string = hashlib.pbkdf2_hmac('sha256', bytes(string),
                                            Config().config['salt'], number_of_rounds)
        return hashed_string
