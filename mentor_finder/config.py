# -*- coding: utf-8 -*-
import os


class Config(object):
    def __init__(self):
        self.config = dict()
        self.config['url'] = self._get_url()
        self.config['salt'] = "DEFAULT_SALT"
        self.config['secret_key'] = self._get_secret_key()
        self.config['mail'] = self._get_mail_config()
        self.config['mail']['port'] = int(self.config['mail']['port'])
        self.config['db_uri'] = self._get_db_uri()

    def _get_mail_config(self):
        prefix = 'MAIL_'
        # These are default values, overwritten by environment vars if they
        # exist
        vars = dict(
            host='http://localhost',
            username='EXAMPLE_MAIL_USERNAME@HOST.COM',
            password='EXAMPLE_MAIL_PASSWORD',
            port=465,
            tls='ssl',
            use='smtp'
        )

        def get_env_var_name(name):
            return prefix + name.upper()

        for var in vars.iterkeys():
            vars[var] = os.getenv(get_env_var_name(var), vars[var])
        return vars

    def _get_secret_key(self):
        return os.getenv('APP_SECRET_KEY', 'omg so secret')

    def _get_url(self):
        return os.getenv('APP_URL', 'http://localhost')

    def _get_db_uri(self):
        return os.getenv('APP_DB_URI',
                         'mongodb://localhost:27017/')
