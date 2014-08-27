# -*- coding: utf-8 -*-
from itsdangerous import URLSafeSerializer
from marrow.mailer import Message
from jinja2 import FileSystemLoader, Environment
from mentor_finder.config import Config


class ActivationMessage(Message):
    def __init__(self, mentor, secret_key=Config().config['secret_key']):
        super(ActivationMessage, self).__init__()
        self.mentor = mentor
        self.secret_key = secret_key

        self.subject = "MentorFinder signup"
        self.plain = self.generate_body_text(mentor)
        self.to = mentor.email
        self.author = Config().config['mail']['username']

    def generate_token(self):
        signer = URLSafeSerializer(self.secret_key)
        return signer.dumps(self.mentor.email)

    def generate_body_text(self, mentor):
        env = Environment(loader=FileSystemLoader(
            'mentor_finder/templates/email'))
        template = env.get_template('activation.txt.jinja2')
        url = "{url}/users/activate/{token}".format(
            url=Config().config['url'],
            token=self.generate_token()
        )
        return template.render(activation_url=url,
                               user=mentor)
