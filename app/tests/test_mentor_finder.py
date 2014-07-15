#!/usr/bin/env python
from .. import mentor_finder
from flask.ext.testing import TestCase

class TestMentorFinder(TestCase):
    def create_app(self):
        app = mentor_finder.app
        app.config['TESTING'] = True
        return app

    def test_landing_page_exists_at_site_root(self):
        root = self.client.get('/')
        assert u'Landing page' in root.data

    def test_signup_page_exists_at_signup(self):
        signup = self.client.get('/mentor_signup')
        assert u'Mentor Signup' in signup.data

    def test_mentor_listings_exist_at_(self):
        mentor_listings = self.client.get('/mentor_listings')
        assert u'Mentor Listings' in mentor_listings.data

#    def test_adding_a_mentor_produces_a_mentor(self):
#        mentor_form_data = dict(
#            email=u"jasongorman@codemanship.com",
#            password=u"apprentice",
#            first_name=u"Jason",
#            second_name=u"Gorman",
#            dob_year=u"1900",
#            dob_month=u"1",
#            dob_day=u"1",
#            description=u"I am a London based software developer \
#            with 22 years commercial experience")
#        self.app.post('/addmentor', data=mentor_form_data)
#        expected_mentor = Mentor(first_name=u"Jason",
#                                 second_name=u"Gorman",
#                                 email=u"jasongorman@codemanship.com",
#                                 dob_year=1900,
#                                 dob_month=1,
#                                 dob_day=1,
#                                 description=u"I am a London based software \
#                                 developer with 22 years commercial \
#                                 experience")
#
#        self.app.get_mentor("jasongorman@codemanship.com")
#        self.assertEqual(expected_mentor, actual_mentor)


if __name__ == '__main__':
    unittest.main()
