#!/usr/bin/env python
from mock import Mock, patch
import unittest

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

    @unittest.skip('Need to fix patching')
    @patch('mentor_finder.views.activate_mentor')
    def test_visiting_user_activate_url_activates_user(self,  activate_mentor):
        token = "EXAMPLE_URLSAFE_TOKEN"
        self.client.get('/users/activate/' + token)
        activate_mentor.assert_called_once_with(token)
