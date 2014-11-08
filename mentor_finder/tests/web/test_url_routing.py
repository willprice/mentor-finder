#!/usr/bin/env python
# -*- coding: utf-8 -*-
from mock import Mock

from mentor_finder.tests.testcases.flask_testcase import FlaskTestCase


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

    def test_visiting_user_activate_url_activates_user(self):
        self.finder.controller.activate_mentor = Mock()
        token = "EXAMPLE_URLSAFE_TOKEN"
        url = '/users/activate/' + token
        self.client.get(url)
        self.finder.controller.activate_mentor.assert_called_once_with(token)

#    def test_current_mentor_is_highlighted_on_listings_page(self):
#        self.finder.app
