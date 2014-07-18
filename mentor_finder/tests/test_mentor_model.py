import unittest
from nose_parameterized import parameterized
import datetime
import utilities


class TestMentorModel(unittest.TestCase):
    @parameterized.expand([
        ("Jason Gorman", "Jason", "Gorman"),
        ("jason Gorman", "jason", "Gorman"),
        ("John James", "John", "James")
    ])
    def test_stores_name(self, expected_name, first_name, last_name):
        jason = utilities.create_example_mentor(
            first_name=first_name,
            last_name=last_name)
        self.assertEqual(expected_name, str(jason.name))

    @parameterized.expand([
        ("jasongorman@codemanship.com",),
        ("jason@jason.com",),
    ])
    def test_stores_email(self, email):
        jason = utilities.create_example_mentor(email=email)
        self.assertEqual(email, jason.email)

    @parameterized.expand([
        ("Greater London"),
        ("Birmingham"),
    ])
    def test_stores_county(self, county):
        jason = utilities.create_example_mentor(county=county)
        self.assertEqual(county, jason.county)

    @parameterized.expand([
        ("I am a London based software developer and trainer with 22 years of commercial experience"),
        ("I have no experience!")
    ])
    def test_stores_description(self, description):
        jason = utilities.create_example_mentor(description=description)
        self.assertEqual(description, jason.description)

    @parameterized.expand([
        [datetime.date(1900, 01, 01)],
        [datetime.date(1900, 12, 30)]
    ])
    def test_stores_date_of_birth(self, date):
        jason = utilities.create_example_mentor(date_of_birth=date)
        self.assertEqual(date, jason.date_of_birth)

    @parameterized.expand([
        (["tdd"], "tdd"),
        (["tdd", "xp"], "tdd,xp"),
    ])
    def test_stores_keywords(self, expected, keywords):
        jason = utilities.create_example_mentor(keywords=keywords)
        self.assertEqual(expected, jason.keywords)


    @parameterized.expand([
        ["parlezuml.com/blog"],
        ["willprice.org"]
    ])
    def test_stores_personal_site(self, site):
        jason = utilities.create_example_mentor(personal_site=site)
        self.assertEqual(site, jason.personal_site)


    @parameterized.expand([
        ["jasongorman"],
        ["will_price_94"]
    ])
    def test_stores_twitter_id(self, twitter_id):
        jason = utilities.create_example_mentor(twitter_id=twitter_id)
        self.assertEqual(twitter_id, jason.twitter_id)


    @parameterized.expand([
        ["jasongorman"],
#        ["will-price"]
    ])
    def test_stores_linkedin_id(self, id):
        jason = utilities.create_example_mentor(linkedin_id=id)
        self.assertEqual(id, jason.linkedin_id)

    def test_twitter_id_is_optional(self):
        utilities.create_minimal_example_mentor(personal_site="parlezuml.com/blog",
                                                keywords="tdd")
        self.assertTrue("twitter_id is not optional")

    def test_personal_site_is_optional(self):
        utilities.create_minimal_example_mentor(keywords="tdd")
        self.assertTrue("personal_site is not optional")

    def test_keywords_are_optional(self):
        utilities.create_minimal_example_mentor()
        self.assertTrue("keywords aren't optional")
