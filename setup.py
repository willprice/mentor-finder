#!/usr/bin/env python2

from distutils.core import setup

setup(name='MentorFinder',
      version='0.1',
      description='Web app to match mentors to students',
      author='Will Price',
      author_email='will.price94+mentorfinder@gmail.com',
      url='www.github.com/willprice/mentor-finder',
      packages=['mentor_finder',
                'mentor_finder.models',
                'mentor_finder.templates',
                'mentor_finder.views'],
     )
