import unittest
from nose_parameterized import parameterized
from jinja2 import Environment, FileSystemLoader
import lxml.html


class TestMentorSignup(unittest.TestCase):
    error_xpath = "//div[@class='error']"
    env = Environment(loader=FileSystemLoader('mentor_finder/templates'))
    template = env.get_template('mentor_signup.html')


    @parameterized.expand([
        [1, "some error message"],
        [0, None]
    ])
    def test_error_div_is_created_only_if_an_error_is_present(self, number_of_errors, error):
        error_divs = self.retrieve_error_divs(error=error)
        self.assertEqual(number_of_errors, len(error_divs))

    def test_error_message_populates_error_div(self):
        message = "Some error message"
        error_divs = self.retrieve_error_divs(error=message)
        error_div_text = error_divs[0].text
        self.assertIn(message, error_div_text)

    def retrieve_error_divs(self, **render_kwargs):
        return self.retrieve_element_from_rendered_html(self.error_xpath, **render_kwargs)

    def retrieve_element_from_rendered_html(self, xpath, **render_kwargs):
        tree = self.render_mentor_signup_page(**render_kwargs)
        return tree.xpath(xpath)

    def render_mentor_signup_page(self, **render_kwargs):
        html = self.template.render(**render_kwargs)
        return lxml.html.fromstring(html)


