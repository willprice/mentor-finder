# -*- coding: utf-8 -*-
from flask import url_for

from mentor_finder import MentorFinder

def serve_static_files():
    url_for('static', filename='css/main.css')
    url_for('static', filename='css/normalize.css')

finder = MentorFinder()
app = finder.app
app.debug = True

try:
    from mentor_finder.sensitive.passes import add_sensitive_information_to_app
    add_sensitive_information_to_app(app)
except ImportError:
    print "Sensitive passes not found, continuing without, expect errors!"

app.run()
serve_static_files()

# vim: set ft=python
