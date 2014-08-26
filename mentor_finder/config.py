# -*- coding: utf-8 -*-
import json
import os


class Config(object):
    def __init__(self):
        self.config = dict()
        self.config ['secret_key'] = self._get_secret_key()
        self.config['mail'] = self._get_mail_config()
        self.config['mail']['port'] = int(self.config['mail']['port'])

    def _get_mail_config(self):
        prefix = 'MAIL_'
        var_names = ['host', 'username', 'password', 'port', 'tls', 'use']
        env_var_names = map(lambda name: (prefix + name).upper(), var_names)
        return dict((name, var) for name, var in
                    zip(var_names, map(lambda var_name: os.getenv(var_name, ''),
                                       env_var_names)
                    )
        )

    def _get_secret_key(self):
        return os.getenv('APP_SECRET_KEY')
