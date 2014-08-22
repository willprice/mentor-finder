# -*- coding: utf-8 -*-
import os
import sys
import new
import sauceclient
import unittest


class SauceConfig(object):
    def __init__(self):
        self.username = self.get_username()
        self.access_key = self.get_access_key()
        if self.can_use_sauce():
            self.sauce = sauceclient.SauceClient(self.username,
                                                 self.access_key)
        else:
            self.sauce = None

    def get_username(self):
        return os.getenv('SAUCE_USERNAME')


    def get_access_key(self):
        return os.getenv('SAUCE_ACCESS_KEY')

    def can_use_sauce(self):
        return self.username and self.access_key


def on_platforms(sauce_config, platforms):
    if sauce_config.can_use_sauce():
        def decorator(base_class):
            module = sys.modules[base_class.__module__].__dict__
            for i, platform in enumerate(platforms):
                d = dict(base_class.__dict__)
                d['desired_capabilities'] = platform
                name = "%s_%s" % (base_class.__name__, i + 1)
                module[name] = new.classobj(name, (base_class,), d)
    else:
        def decorator(base_class):
            module = sys.modules[base_class.__module__].__dict__
            name = base_class.__name__
            # A '_' is appended to make nose pick up the test,
            # if you don't modify the name it doesn't work.
            module[name + '_'] = new.classobj(name,
                                        (base_class,
                                         unittest.TestCase),
                                        dict(base_class.__dict__))
    return decorator
