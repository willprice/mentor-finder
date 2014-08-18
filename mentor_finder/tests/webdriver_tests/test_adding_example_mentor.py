from mentor_finder.tests.flask_testcase import FlaskTestCase
from flask.ext.testing import LiveServerTestCase
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException, NoAlertPresentException
import unittest, time, re


class TestAddingExampleMentor(LiveServerTestCase, FlaskTestCase):
    def create_app(self):
        super(FlaskTestCase, self).__init__()
        self.app['LIVESERVER_PORT'] = 8943
        super(LiveServerTestCase, self).__init__()

    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)
        self.base_url = "http://localhost:8943"
        self.verificationErrors = []
        self.accept_next_alert = True

    def test_adding_example_mentor(self):
        driver = self.driver
        driver.get(self.base_url + "/")
        driver.find_element_by_css_selector("a > div.enter_button").click()
        driver.find_element_by_id("email").send_keys("will.price94@gmail.com")
        driver.find_element_by_id("password").send_keys("apprentice")
        driver.find_element_by_id("password_confirmation").send_keys("apprentice")
        driver.find_element_by_id("first_name").send_keys("Will")
        driver.find_element_by_id("last_name").send_keys("Price")
        Select(driver.find_element_by_id("county")).select_by_visible_text("Herefordshire")
        driver.find_element_by_id("date_of_birth").send_keys("1994-04-26")
        driver.find_element_by_id("description").send_keys("Hi, I'm an aspiring software developer who would love to mentor people")
        driver.find_element_by_id("keywords").send_keys("XP,eXtreme Programming,TDD,Test driven development,Refactoring,Python,js")
        driver.find_element_by_id("personal_site").send_keys("http://willprice.org")
        driver.find_element_by_id("twitter_id").send_keys("will_price_94")
        driver.find_element_by_id("linkedin").send_keys("http://uk.linkedin.com/pub/will-price/7b/579/aba/")
        driver.find_element_by_id("github_id").send_keys("willprice")
        driver.find_element_by_css_selector("input[type=\"submit\"]").click()
        # ERROR: Caught exception [unknown command []]

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
