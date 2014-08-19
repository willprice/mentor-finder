import flask_testcase
import mentor_finder
from mentor_finder.models.name import Name
import datetime


class AcceptanceTest(flask_testcase.FlaskTestCase):
    def test_adding_a_mentor_produces_a_mentor(self):
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
        actual_mentor = self.finder.controller.faculty.get_mentor(
            mentor_form_data['email'])

        self.assertIsNotNone(actual_mentor)
        self.assertEqual(u"jasongorman@codemanship.com", actual_mentor.email)
        self.assertEqual(Name(u"Jason", u"Gorman"), actual_mentor.name)
        self.assertEqual(u"Greater London", actual_mentor.county)
        self.assertEqual(datetime.datetime(1900, 01, 01), actual_mentor.date_of_birth)
        self.assertEqual(["tdd", "xp"], actual_mentor.keywords)
        self.assertEqual("parlezuml.com/blog", actual_mentor.personal_site)
        self.assertEqual("jasongorman", actual_mentor.twitter_id)

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
