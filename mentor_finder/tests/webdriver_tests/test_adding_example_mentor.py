# -*- coding: utf-8 -*-
import unittest
import multiprocessing
import time


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
    def _spawn_live_server(self):
        self._process = None
        self.port = self.app.config.get('LIVESERVER_PORT', 5000)

        worker = lambda app, port: app.run(port=port, host='0.0.0.0')

        self._process = multiprocessing.Process(
            target=worker, args=(self.app, self.port)
        )

        self._process.start()

        # we must wait the server start listening
        time.sleep(1)

    def setUp(self):
        LiveServerTestCase.__init__(self)

    def create_app(self):
        app = FlaskTestCase.create_app(self)
        app.config['LIVESERVER_PORT'] = 3000
        return app

    def setUp(self):
        if sauce_config.can_use_sauce():
            self.desired_capabilities['name'] = self.id()
            sauce_url = "http://%s:%s@ondemand.saucelabs.com:80/wd/hub"
            self.driver = webdriver.Remote(
                desired_capabilities=self.desired_capabilities,
                command_executor=sauce_url % (
                    sauce_config.username,
                    sauce_config.access_key
                ),
            )
            self.using_sauce = True
        else:
            self.driver = webdriver.Firefox()
            self.using_sauce = False

        self.base_url = "http://0.0.0.0:%s" % self.app.config['LIVESERVER_PORT']
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

    def test_cancelling_submission(self):
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
