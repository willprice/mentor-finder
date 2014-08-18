#!/usr/bin/env python
from flask_testing import LiveServerTestCase
from mentor_finder.tests.flask_testcase import FlaskTestCase


class TestMentorFinder(FlaskTestCase):
    def test_landing_page_exists_at_site_root(self):
        root = self.client.get('/')
        assert u'Landing page' in root.data

    def test_signup_page_exists_at_signup(self):
        signup = self.client.get('/mentor_signup')
        assert u'Mentor Signup' in signup.data

    def test_mentor_listings_exist_at_(self):
        mentor_listings = self.client.get('/mentor_listings')
        assert u'Mentor Listings' in mentor_listings.data
