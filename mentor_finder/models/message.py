# -*- coding: utf-8 -*-
from itsdangerous import URLSafeSerializer
from marrow.mailer import Message
from jinja2 import FileSystemLoader, Environment


class ActivationMessage(Message):
    def __init__(self, mentor, secret_key):
        self.mentor = mentor
        self.secret_key = secret_key

        super(ActivationMessage, self).__init__(to=mentor.email)

        self.token = self.generate_token()
        self.plain = self.generate_body_text(mentor)

    def generate_token(self):
        signer = URLSafeSerializer(self.secret_key)
        return signer.dumps(self.mentor.email)

    def generate_body_text(self, mentor):
        env = Environment(loader=FileSystemLoader(
            'mentor_finder/templates/email'))
        template = env.get_template('activation.txt.jinja2')
        return template.render(activation_url=self.token,
                                     user=mentor)
