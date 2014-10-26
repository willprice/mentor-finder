# -*- coding: utf-8 -*-
from mentor_finder.tests.testcases import flask_testcase


class AcceptanceTest(flask_testcase.FlaskTestCase):
    def test_adding_same_mentor_twice_produces_an_error_div_on_signup_page(self):
        response = self.client.get('/mentor_signup')
        self.assert200(response)
        mentor_form_data = dict(
            email=u"jasongorman@codemanship.com",
            password=u"apprentice",
            password_confirmation=u"apprentice",
            first_name=u"Jason",
            last_name=u"Gorman",
            county=u"Greater London",
            date_of_birth=u"1900-01-01",
            description=u"I am a London based software developer with 22 years commercial experience",
            keywords=u"tdd,xp",
            personal_site="parlezuml.com/blog",
            twitter_id="jasongorman"
        )
        self.client.post('/mentor_signup', data=mentor_form_data)
        response = self.client.post('/mentor_signup', data=mentor_form_data)
        self.assertIn("email address has already been registered", response.data)
