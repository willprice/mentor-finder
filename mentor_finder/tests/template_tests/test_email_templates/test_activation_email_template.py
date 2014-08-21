# -*- coding: utf-8 -*-
from jinja2 import Environment, FileSystemLoader

from mentor_finder.tests.template_testcase import TemplateTestCase
from mentor_finder.tests.util import create_example_mentor


class TestActivationEmail(TemplateTestCase):
    env = Environment(loader=FileSystemLoader('mentor_finder/templates'))
    template = env.get_template('email/activation.txt.jinja2')

    def setUp(self):
        self.user = create_example_mentor()

    def test_contains_the_users_name(self):
        self.assertIn(self.user.name.first, self.template.render(
            user=self.user)
        )

    def test_contains_activation_url(self):
        example_url = 'http://EXAMPLE.COM/' + str(self.user.name) + \
                      'aklsdjDLSKFJSLDFJlksJDLkjlkopiuwepoiuvnF'
        self.assertIn(example_url, self.template.render(
            user=self.user,
            activation_url=example_url),
        )

    def test_contains_length_of_life_of_token(self):
        length_of_life = str(7)
        self.assertIn(length_of_life, self.template.render(
            user=self.user,
            length_of_token_life_days=length_of_life),
        )
