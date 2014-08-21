# -*- coding: utf-8 -*-
from flask import url_for

from mentor_finder import MentorFinder

finder = MentorFinder()
app = finder.app

try:
    from mentor_finder.sensitive.passes import add_sensitive_information_to_app
    add_sensitive_information_to_app(app)
except ImportError:
    print "Sensitive passes not found, continuing without, expect errors!"
