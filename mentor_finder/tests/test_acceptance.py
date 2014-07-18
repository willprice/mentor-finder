import flask_testcase
import mentor_finder
import mentor_finder.models
import datetime

class AcceptanceTest(flask_testcase.FlaskTestCase):
    def test_adding_a_mentor_produces_a_mentor(self):
        mentor_form_data = dict(
            email=u"jasongorman@codemanship.com",
            password=u"apprentice",
            first_name=u"Jason",
            last_name=u"Gorman",
            county=u"Greater London",
            dob_year=u"1900",
            dob_month=u"1",
            dob_day=u"1",
            description=u"I am a London based software developer with 22 years commercial experience")
        self.client.post('/addmentor', data=mentor_form_data)
        expected_mentor = mentor_finder.models.Mentor.create(dict(
            first_name=u"Jason",
            last_name=u"Gorman",
            email=u"jasongorman@codemanship.com",
            county=u"Greater London",
            date_of_birth=datetime.date(1900, 01, 01),
            description=u"I am a London based software developer with 22 years commercial experience"
        ))

        actual_mentor = mentor_finder.controller.faculty.get_mentor("jasongorman@codemanship.com")
        self.assertEqual(expected_mentor, actual_mentor)
