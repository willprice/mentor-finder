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
            description=u"I am a London based software developer with 22 years commercial experience",
            keywords=u"tdd,xp",
            personal_site="parlezuml.com/blog",
            twitter_id="jasongorman"
        )
        self.client.post('/addmentor', data=mentor_form_data)
        actual_mentor = mentor_finder.controller.faculty.get_mentor("jasongorman@codemanship.com")

        self.assertEqual(u"jasongorman@codemanship.com", actual_mentor.email)
        self.assertEqual(mentor_finder.models.Name(u"Jason", u"Gorman"), actual_mentor.name)
        self.assertEqual(u"Greater London", actual_mentor.county)
        self.assertEqual(datetime.date(1900, 01, 01), actual_mentor.date_of_birth)
        self.assertEqual(["tdd", "xp"], actual_mentor.keywords)
        self.assertEqual("parlezuml.com/blog", actual_mentor.personal_site)
        self.assertEqual("jasongorman", actual_mentor.twitter_id)
