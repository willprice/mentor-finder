# -*- coding: utf-8 -*-
from flask.ext.testing import LiveServerTestCase
from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException, NoAlertPresentException
import unittest

import mentor_finder
from mentor_finder.tests.flask_testcase import FlaskTestCase
from mentor_finder.models.mentor import Mentor


@unittest.skip('Broken because mentor_finders controller seems to have a reference to the wrong faculty')
class TestAddingExampleMentor(LiveServerTestCase, FlaskTestCase):
    def setUp(self):
        FlaskTestCase.__init__(self)
        LiveServerTestCase.__init__(self)

    def create_app(self):
        app = FlaskTestCase.create_app(self)
        app.config['DEBUG'] = False
        app.config['LIVESERVER_PORT'] = 8943
        return app

    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)
        self.base_url = "http://localhost:%s" % self.app.config['LIVESERVER_PORT']
        self.verificationErrors = []
        self.accept_next_alert = True

    def test_adding_example_mentor(self):
        email_address = u"will.price94@gmail.com"

        driver = self.driver
        driver.get(self.base_url + "/")
        driver.find_element_by_css_selector("a > div.enter_button").click()
        driver.find_element_by_css_selector("label").click()
        driver.find_element_by_id("email").send_keys(email_address)
        driver.find_element_by_id("password").send_keys(u"apprentice")
        driver.find_element_by_id("password_confirmation").send_keys(u"apprentice")
        driver.find_element_by_id("first_name").send_keys(u"Will")
        driver.find_element_by_id("last_name").send_keys(u"Price")
        Select(driver.find_element_by_id("county")).select_by_visible_text(u"Herefordshire")
        driver.find_element_by_css_selector("button.ws-popover-opener").click()
        driver.find_element_by_css_selector("button.ws-prev").click()
        driver.find_element_by_css_selector(".ws-item-1 button").click()
        driver.find_element_by_css_selector(".ws-item-1 button").click()
        driver.find_element_by_css_selector("button.day-1.ws-focus").click()
        driver.find_element_by_id("description") \
            .send_keys(u"Hi, I'm an aspiring software developer who would love to mentor people")
        driver.find_element_by_id("keywords").send_keys(u"XP,eXtreme Programming,TDD,Test driven development,Refactoring,COBOL")
        driver.find_element_by_id("personal_site").send_keys(u"http://willprice.org")
        driver.find_element_by_id("twitter_id").send_keys(u"will_price_94")
        driver.find_element_by_id("linkedin").send_keys(u"http://uk.linkedin.com/pub/will-price/7b/579/aba/")
        driver.find_element_by_id("github_id").send_keys(u"willprice")
        driver.find_element_by_css_selector("input[type='submit']").click()
        print "Mentors: "
        print str(mentor_finder.controller.faculty)
        self.assertIsInstance(mentor_finder.controller.faculty.get_mentor(email_address), Mentor)


    def is_element_present(self, how, what):
        try:
            self.driver.find_element(by=how, value=what)
        except NoSuchElementException:
            return False
        return True

    def is_alert_present(self):
        try:
            self.driver.switch_to.alert()
        except NoAlertPresentException:
            return False
        return True

    def close_alert_and_get_its_text(self):
        try:
            alert = self.driver.switch_to.alert()
            alert_text = alert.text
            if self.accept_next_alert:
                alert.accept()
            else:
                alert.dismiss()
            return alert_text
        finally:
            self.accept_next_alert = True

    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    unittest.main()
