#!/usr/bin/env python2
from flask.ext.script import Manager
import subprocess

import mentor_finder.wsgi
NOSE_ARGS = ['--exe', '--with-coverage', '--cover-package=mentor_finder']

manager = Manager(mentor_finder.wsgi.app)

@manager.command
def run():
    mentor_finder.main()

@manager.command
def test():
   subprocess.call(["nosetests"] + NOSE_ARGS)


if __name__ == "__main__":
    manager.run()
