# -*- coding: utf-8 -*-
import unittest
from nose_parameterized import parameterized
from jinja2 import Environment, FileSystemLoader

import mentor_finder.tests.util as utilities
from mentor_finder.tests.testcases.template_testcase import TemplateTestCase

import lxml.html



class TestMentorListings(TemplateTestCase):
    mentor_divs_xpath = "//div[@id='content']/div[contains(@class, 'mentor')]"
    env = Environment(loader=FileSystemLoader('mentor_finder/templates'))
    template = env.get_template('mentor_listings.html')

    @parameterized.expand([
        (1, [utilities.create_example_mentor()]),
        (2, [utilities.create_example_mentor(), utilities.create_example_mentor()])
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
        self.assertIn(first_name, self.flatten_text(mentor_div))

    @parameterized.expand([
        ("Greater London",),
        ("Herefordshire",)
    ])
    def test_mentor_county_is_present_in_mentor_div(self, county):
        example_mentor = utilities.create_example_mentor(county=county)
        mentor_div = self.render_template_and_return_mentor_divs([example_mentor])[0]
        self.assertIn(county, self.flatten_text(mentor_div))

    @parameterized.expand([
        ("jasongorman@codemanship.com",),
        ("jason@jason.com",)
    ])
    def test_mentor_email_is_present_in_mentor_div(self, email):
        example_mentor = utilities.create_example_mentor(email=email)
        mentor_div = self.render_template_and_return_mentor_divs([example_mentor])[0]
        self.assertIn(email, self.flatten_text(mentor_div))

    @parameterized.expand([
        ("I am a london based ...",),
        ("I don't like to divulge professional information",)
    ])
    def test_mentor_description_is_present_in_mentor_div(self, description):
        example_mentor = utilities.create_example_mentor(description=description)
        mentor_div = self.render_template_and_return_mentor_divs([example_mentor])[0]
        self.assertIn(description, self.flatten_text(mentor_div))

    @parameterized.expand([
        ("jasongorman",),
        ("will_price_94",)
    ])
    def test_twitter_id_populates_a_link(self, id):
        example_mentor = utilities.create_example_mentor(twitter_id=id)
        mentor_div = self.render_template_and_return_mentor_divs([example_mentor])[0]
        self.assertIn(id, self.flatten_text(mentor_div))

    @parameterized.expand([
        ("parlezuml.com/blog",),
        ("willprice.org",)
    ])
    def test_site_url_is_present_in_listing(self, site):
        example_mentor = utilities.create_example_mentor(personal_site=site)
        mentor_div = self.render_template_and_return_mentor_divs([example_mentor])[0]
        self.assertIn(site, self.flatten_text(mentor_div))

    @parameterized.expand([
        (["Programming", "TDD", "Refactoring"],),
        (["COBOL", "Agile"],)
    ])
    def test_keywords_are_present_in_list(self, keywords):
        example_mentor = utilities.create_example_mentor(keywords=", ".join(keywords))
        mentor_div = self.render_template_and_return_mentor_divs([example_mentor])[0]
        for keyword in keywords:
            self.assertIn(keyword, self.flatten_text(mentor_div))

    @parameterized.expand([
        ["linkedin_url_1"],
        ["linkedin_url_2"],
    ])
    def test_linkedin_url_is_present_in_listing(self, linkedin):
        example_mentor = utilities.create_example_mentor(linkedin=linkedin)
        mentor_div = self.render_template_and_return_mentor_divs([example_mentor])[0]
        self.assertIn(linkedin, self.flatten_text(mentor_div))

    @parameterized.expand([
        ["jasongorman"],
        ["willprice"]
    ])
    def test_github_url_is_present_in_listing(self, github_id):
        example_mentor = utilities.create_example_mentor(github_id=github_id)
        mentor_div = self.render_template_and_return_mentor_divs([example_mentor])[0]
        self.assertIn("http://github.com/{}".format(github_id), self.flatten_text(mentor_div))

    def test_current_mentor_is_highlighted(self):
        example_mentor = utilities.create_example_mentor()
        mentor_div = self.render_template_and_return_mentor_divs([example_mentor], current=example_mentor)[0]
        self.assertIn("highlight", mentor_div.attrib['class'])

    def test_only_the_current_mentor_is_highlighted(self):
        example_mentor = utilities.create_example_mentor()
        another_mentor = utilities.create_example_mentor(email="jo@jo.com")
        another_mentor_div = self.render_template_and_return_mentor_divs([example_mentor, another_mentor], current=example_mentor)[1]
        self.assertNotIn("highlight", another_mentor_div.attrib['class'])

    def test_only_activated_mentors_are_shown(self):
        example_mentor = utilities.create_example_mentor(not_activated=True)
        mentor_divs = self.render_template_and_return_mentor_divs([example_mentor])
        self.assertEqual(0, len(mentor_divs))


    def render_template_and_return_mentor_divs(self, mentors, **kwargs):
        tree = self.render_html_to_tree(mentors, **kwargs)
        mentor_divs = tree.xpath(self.mentor_divs_xpath)
        return mentor_divs

    def render_html_to_tree(self, mentors, **kwargs):
        html = self.render_template_with_mentors(mentors, **kwargs)
        tree = lxml.html.fromstring(html)
        return tree

    def render_template_with_mentors(self, mentors, **kwargs):
        return self.template.render(mentors=mentors, **kwargs)

