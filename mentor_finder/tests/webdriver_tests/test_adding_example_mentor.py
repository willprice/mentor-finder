# -*- coding: utf-8 -*-
import unittest

from flask.ext.testing import LiveServerTestCase
from selenium import webdriver
from selenium.webdriver.support.ui import Select

from mentor_finder.tests.flask_testcase import FlaskTestCase
from mentor_finder.tests.sauce_config import SauceConfig, on_platforms


browsers = [{"platform": "Mac OS X 10.9",
             "browserName": "chrome",
             "version": "31"},
            {"platform": "Linux",
             "browserName": "firefox",
             "version": "31"},
            {"platform": "Windows 8.1",
             "browserName": "internet explorer",
             "version": "11"}]
sauce_config = SauceConfig()


@on_platforms(sauce_config, browsers)
class TestAddingExampleMentor(LiveServerTestCase, FlaskTestCase):
    def setUp(self):
        LiveServerTestCase.__init__(self)

    def create_app(self):
        app = FlaskTestCase.create_app(self)
        app.config['LIVESERVER_PORT'] = 8111
        return app

    def setUp(self):
        if sauce_config.can_use_sauce():
            sauce_url = "http://%s:%s@ondemand.saucelabs.com:80/wd/hub"
            self.driver = webdriver.Remote(
                desired_capabilities=self.desired_capabilities,
                command_executor=sauce_url % (
                    sauce_config.username,
                    sauce_config.access_key
                )
            )
            self.using_sauce = True
        else:
            self.driver = webdriver.Firefox()
            self.base_url = "http://localhost:%s" % self.app.config['LIVESERVER_PORT']
            self.using_sauce = False

        self.driver.implicitly_wait(30)
        self.verificationErrors = []
        self.accept_next_alert = True

    def test_adding_example_mentor(self):
        email_address = u"will.price94@gmail.com"

        driver = self.driver
        self.visit_landing_page(driver)
        self.landing_page_to_mentor_signup(driver)
        self.fill_mentor_signup_form_with_valid_details(driver,
                                                        email_address)
        driver.find_element_by_css_selector("input[type='submit']").click()
        email = driver.find_element_by_class_name("email")
        self.assertEqual(email_address, email.text)

    def test_cancelling_submition(self):
        email_address = u"will.price94@gmail.com"

        driver = self.driver
        driver.get(self.base_url + "/")
        self.landing_page_to_mentor_signup(driver)
        self.fill_mentor_signup_form_with_valid_details(driver,
                                                        email_address)
        driver.find_element_by_id("cancel").click()
        self.assertTrue(driver.find_element_by_id("landing"))

    def visit_landing_page(self, driver):
        driver.get(self.base_url + "/")

    def landing_page_to_mentor_signup(self, driver):
        driver.find_element_by_css_selector(
            "a > div.enter_button").click()

    def fill_mentor_signup_form_with_valid_details(self, driver,
                                                   email_address):
        driver.find_element_by_id("email").send_keys(email_address)
        driver.find_element_by_id("password").send_keys(u"apprentice")
        driver.find_element_by_id("password_confirmation").send_keys(
            u"apprentice")
        driver.find_element_by_id("first_name").send_keys(u"Will")
        driver.find_element_by_id("last_name").send_keys(u"Price")
        Select(
            driver.find_element_by_id("county")).select_by_visible_text(
            u"Herefordshire")
        driver.find_element_by_css_selector(
            "button.ws-popover-opener").click()
        driver.find_element_by_css_selector("button.ws-prev").click()
        driver.find_element_by_css_selector(".ws-item-1 button").click()
        driver.find_element_by_css_selector(".ws-item-1 button").click()
        driver.find_element_by_css_selector(
            "button.day-1.ws-focus").click()
        driver.find_element_by_id("description") \
            .send_keys(
            u"Hi, I'm an aspiring software developer who would love to mentor people")
        driver.find_element_by_id("keywords").send_keys(
            u"XP,eXtreme Programming,TDD,Test driven development,Refactoring,COBOL")
        driver.find_element_by_id("personal_site").send_keys(
            u"http://willprice.org")
        driver.find_element_by_id("twitter_id").send_keys(
            u"will_price_94")
        driver.find_element_by_id("linkedin").send_keys(
            u"http://uk.linkedin.com/pub/will-price/7b/579/aba/")
        driver.find_element_by_id("github_id").send_keys(u"willprice")

    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    unittest.main()
