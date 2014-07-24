from jinja2 import Environment, FileSystemLoader
from mentor_finder.models.forms.mentor_signup import mentor_signup_form_factory
from mentor_finder.models.faculty import Faculty
from mentor_finder.tests.template_testcase import TemplateTestCase
from mentor_finder.tests.flask_testcase import FlaskTestCase
import lxml.html

MentorSignupTemplate = mentor_signup_form_factory(Faculty())

class TestMentorSignupTemplate(TemplateTestCase, FlaskTestCase):
    env = Environment(loader=FileSystemLoader('mentor_finder/templates'))
    template = env.get_template('mentor_signup.html')

    def test_error_div_isnt_present_normally(self):
        html = self.template.render(form=MentorSignupTemplate())
        tree = lxml.html.fromstring(html)
        self.assertFalse(tree.xpath('//div[id="error"]'))
