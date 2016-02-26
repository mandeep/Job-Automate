import unittest
from indeed import IndeedClient
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
from jobautomate.jobautomate import indeed_parameters, indeed_urls


class JobAutomateTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Firefox()

    def tearDown(self):
        self.driver.quit()

    def test_parameters(self):
        self.assertIsNotNone(indeed_parameters)

    def test_api(self):
        self.assertTrue(len(indeed_urls(indeed_parameters("python developer", ""))) > 1)

    def test_api_again(self):
        self.assertFalse(len(indeed_urls(indeed_parameters("job_does_not_exist", "location_does_not_exit"))) > 1)


if __name__ == "__main__":
    unittest.main()
