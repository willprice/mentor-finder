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


