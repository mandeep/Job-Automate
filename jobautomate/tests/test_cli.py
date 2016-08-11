import unittest
from unittest.mock import patch
from indeed import IndeedClient
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
import jobautomate.commandline


class JobAutomateTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Firefox()

    def tearDown(self):
        self.driver.quit()

    def test_parameters(self):
        self.assertIsNotNone(jobautomate.commandline.
                             indeed_parameters('Software Developer', 'USA'))
    def test_urls_retrieval(self):
        self.assertIsNotNone(jobautomate.commandline.indeed_urls(jobautomate.commandline.
                                                                 indeed_parameters('Software Developer', 'USA')))
