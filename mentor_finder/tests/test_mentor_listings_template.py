import unittest
from nose_parameterized import parameterized
from jinja2 import Environment, FileSystemLoader

import mentor_finder
import utilities

import lxml.html


class TestMentorListings(unittest.TestCase):
    mentor_divs_xpath = "//div[@id='content']/div[@class='mentor']"

    def setUp(self):
        self.hi = "hi"
        # app is the name of the package that is imported since the templates
        # are in the top level directory we don't care, so can import anything
        # here
        self.env = Environment(loader=FileSystemLoader('mentor_finder/templates'))
        self.template = self.env.get_template('mentor_listings.html')

    @parameterized.expand([
        (1, [None]),
        (2, [None, None])
    ])
    def test_there_are_the_same_number_of_mentor_divs_as_mentors(self, expected_number_of_mentor_divs, mentors):
        mentor_divs = self.render_template_and_return_mentor_divs(mentors)
        self.assertEqual(expected_number_of_mentor_divs, len(mentor_divs))

    @parameterized.expand([
        ("Jason",),
        ("Billy",)
    ])
    def test_mentor_name_is_present_in_mentor_div(self, first_name):
        example_mentor = utilities.create_example_mentor(first_name=first_name)
        mentor_div = self.render_template_and_return_mentor_divs([example_mentor])[0]
        self.assertIn(str(example_mentor.name), self.flatten_text(mentor_div))

    @parameterized.expand([
        ("Greater London"),
        ("Herefordshire")
    ])
    def test_mentor_county_is_present_in_mentor_div(self, county):
        example_mentor = utilities.create_example_mentor(county=county)
        mentor_div = self.render_template_and_return_mentor_divs([example_mentor])[0]
        self.assertIn(example_mentor.county, self.flatten_text(mentor_div))

    @parameterized.expand([
        ("jasongorman@codemanship.com",),
        ("jason@jason.com",)
    ])
    def test_mentor_email_is_present_in_mentor_div(self, email):
        example_mentor = utilities.create_example_mentor(email=email)
        mentor_div = self.render_template_and_return_mentor_divs([example_mentor])[0]
        self.assertIn(example_mentor.email, self.flatten_text(mentor_div))

    @parameterized.expand([
        ("I am a london based ..."),
        ("I don't like to divulge professional information")
    ])
    def test_mentor_description_is_present_in_mentor_div(self, description):
        example_mentor = utilities.create_example_mentor(description=description)
        mentor_div = self.render_template_and_return_mentor_divs([example_mentor])[0]
        self.assertIn(example_mentor.description, self.flatten_text(mentor_div))

    def create_app(self):
        app = mentor_finder.app
        app.config['TESTING'] = True
        return app

    def flatten_text(self, element):
        text = element.text
        for child in element:
            text += self.flatten_text(child)
        return text

    def render_template_and_return_mentor_divs(self, mentors):
        html = self.render_template_with_mentors(mentors)
        tree = lxml.html.fromstring(html)
        mentor_divs = tree.xpath(self.mentor_divs_xpath)
        return mentor_divs

    def render_template_with_mentors(self, mentors):
        return self.template.render(mentors=mentors)

