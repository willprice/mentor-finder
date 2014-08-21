#!/usr/bin/env python2
from flask.ext.script import Manager
import subprocess

NOSE_ARGS = ['--exe',
             '--with-coverage',
             '--cover-package=mentor_finder',
             ]

import mentor_finder.wsgi
manager = Manager(mentor_finder.wsgi.app)

@manager.command
def run():
    mentor_finder.wsgi.app.run(debug=True)

@manager.command
def unittest():
   subprocess.call(["nosetests"] +
                   NOSE_ARGS +
                   ['--exclude-dir=mentor_finder/tests/webdriver_tests'])

@manager.command
def functionaltest():
   subprocess.call(["nosetests"] + NOSE_ARGS +
   ['mentor_finder/tests/webdriver_tests'])


if __name__ == "__main__":
    manager.run()
