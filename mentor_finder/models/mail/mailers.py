# -*- coding: utf-8 -*-
from marrow.mailer import Mailer as MarrowMailer
import time
from mentor_finder.config import Config


class Mailer(object):
    def __init__(self):
        self.config = Config().config['mail']
        self.mailer = MarrowMailer(
            dict(
                transport=dict(debug=True,
                               **self.config),
                manager=dict(),
                ),
            )

    def send(self, message):
        self.mailer.start()
        self.mailer.send(message)
        self.mailer.stop()
        pass

class StubMailer(object):
    def __init__(self):
        pass

    def send(self, message):
        pass
