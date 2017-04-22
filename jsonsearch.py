import unittest
from selenium import webdriver
import webbrowser

url = 'https://www.facebook.com/'

webbrowser.open_new(url)

AmberTest.setUpClass

AmberTest.test_title


AmberTest.test_search


class AmberTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Safari()

    def test_title(self):
        self.driver.get('https://www.google.com')

    def test_search(self):
            self.driver.get('https://www.google.com/search.htm')
            search_input = self.driver.find_element_by_css_selector
            '#content input[type="text"]')
            search_input.send_keys('Meet the Team')
            search_submit = self.driver.find_element_by_css_selector(

        '#content input[type="submit"]')
        search_submit.click()
        self.assertTrue(self.driver.find_element_by_css_selector(
            'a[href="http://www.aweber.com/meet-the-team.htm"]'))