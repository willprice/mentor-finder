import lxml.html
from flask import render_template
from mentor_finder.web import flash_errors

from mentor_finder.views.forms.mentor_signup import mentor_signup_form_factory
from mentor_finder.models.faculty import Faculty
from mentor_finder.tests.template_testcase import TemplateTestCase
from mentor_finder.tests.flask_testcase import FlaskTestCase


MentorSignupForm = mentor_signup_form_factory(Faculty())

class TestMentorSignupTemplate(TemplateTestCase, FlaskTestCase):
    error_div_xpath = '//div[@class="error"]'

    def test_flashed_error_creates_an_error_div(self):
        form = MentorSignupForm()
        form.process(name="john*`")
        form.validate()
        flash_errors(form)

        html = render_template('mentor_signup.html', form=form)
        print html
        tree = lxml.html.fromstring(html)
        number_of_error_divs = tree.xpath(self.error_div_xpath)
        self.assertGreater(len(number_of_error_divs), 1)

    def test_error_div_isnt_present_normally(self):
        html = render_template('mentor_signup.html', form=MentorSignupForm())
        tree = lxml.html.fromstring(html)
        self.assertFalse(tree.xpath(self.error_div_xpath))

