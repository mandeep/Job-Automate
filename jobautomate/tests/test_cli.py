import jobautomate.commandline
from selenium.common.exceptions import NoSuchElementException
import pytest


class TestJobAutomate:

    def test_indeed_api_parameters(self):
        parameters = jobautomate.commandline.indeed_parameters('Financial Analyst', 'New York City')
        assert isinstance(parameters, dict) is True
        assert 'Financial Analyst' in parameters.values()
        assert 'New York City' in parameters.values()

    def test_indeed_api_urls(self):
        parameters = jobautomate.commandline.indeed_parameters('Financial Analyst', 'New York City')
        job_urls = jobautomate.commandline.indeed_urls(parameters)
        assert len(job_urls) > 1
        for url in job_urls:
            assert 'http://' in url

    def test_indeed_apply_button(self, selenium):
        selenium.get(
            "http://www.indeed.com/cmp/Discover-Books/jobs/Full-Time-Driver-3ce56851d8772139")
        selenium.implicitly_wait(7)
        try:
            jobautomate.commandline.find_apply_button(selenium, 'indeed-apply-button')
        except NoSuchElementException:
            pytest.fail('NoSuchElementException')
