# -*- coding: utf-8 -*-
import unittest
import mock
from mentor_finder.controller import Controller


class TestSignupErrorReporting(unittest.TestCase):
    def test_invalid_form_triggers_error_reporting(self):
        error_reporter_mock = mock.Mock()
        controller = Controller(None, error_reporter=error_reporter_mock)

        class Form():
            def validate_on_submit(self):
                return False

        form = Form()
        controller.process_mentor_form(form, None, None, lambda : None)
        controller.error_reporter.assert_called_with(form)
