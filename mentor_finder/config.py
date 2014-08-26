# -*- coding: utf-8 -*-
import json


class Config(object):
    def __init__(self):
        self.config = self.get_config()

    def get_config(self):
        with open('mentor_finder/sensitive/mentor_finder.json') as config_file:
            return json.load(config_file)
