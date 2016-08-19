from click.testing import CliRunner
import jobautomate.commandline
import pytest


@pytest.fixture
def parameters():
    job_search = jobautomate.commandline.indeed_parameters('Financial Analyst', 'New York City')
    return job_search


def fill(driver):
    jobautomate.commandline.find_apply_button(driver, 'indeed-apply-button')
    jobautomate.commandline.switch_frames(driver, 'iframe[name$=modal-iframe]')
    jobautomate.commandline.fill_application(
        driver, 'Homer', 'Simpson', 'Chunkylover53@aol.com', 'resume.txt')


def test_indeed_api_parameters(parameters):
    assert isinstance(parameters, dict) is True
    assert 'Financial Analyst' in parameters.values()
    assert 'New York City' in parameters.values()


def test_indeed_api_urls(parameters):
    job_urls = jobautomate.commandline.indeed_urls(parameters)
    assert len(job_urls) == 25
    for url in job_urls:
        assert 'http://' in url


def test_false_api_key(parameters):
    try:
        jobautomate.commandline.indeed_urls(parameters, 123456789)
    except NameError:
        pass


def test_indeed_apply_button(selenium):
    selenium.get(
        "http://www.indeed.com/cmp/Discover-Books/jobs/Full-Time-Driver-3ce56851d8772139")
    jobautomate.commandline.find_apply_button(selenium, 'indeed-apply-button')


def test_fill_application(selenium):
    selenium.get(
        "http://www.indeed.com/cmp/Discover-Books/jobs/Full-Time-Driver-3ce56851d8772139")
    fill(selenium)


def test_fill_application_again(selenium):
    selenium.get(
        "http://www.indeed.com/viewjob?jk=f6c24d6728d6b55f")
    fill(selenium)


def test_click_apply(selenium):
    selenium.get(
        "http://www.indeed.com/cmp/Discover-Books/jobs/Full-Time-Driver-3ce56851d8772139")
    fill(selenium)
    jobautomate.commandline.apply_or_continue(selenium, debug=True)


def test_click_apply_again(selenium):
    selenium.get(
        "http://www.indeed.com/viewjob?jk=f6c24d6728d6b55f")
    fill(selenium)
    jobautomate.commandline.apply_or_continue(selenium, debug=True)


def test_cli_command():
    runner = CliRunner()
    result = runner.invoke(
        jobautomate.commandline.cli, ['--debug', 'Homer', 'Simpson', 'Chunkylover53@aol.com',
                                      'Nuclear Technician', '.travis.yml'], input='No')
    assert not result.exception


def test_cli_verbose():
    runner = CliRunner()
    verbose_result = runner.invoke(
        jobautomate.commandline.cli, ['--debug', '--verbose', 'Homer', 'Simpson',
                                      'Chunkylover53@aol.com', 'Nuclear Technician',
                                      '.travis.yml'], input='No')
    assert not verbose_result.exception


def test_cli_continue():
    runner = CliRunner()
    continue_result = runner.invoke(
        jobautomate.commandline.cli, ['--debug', 'Homer', 'Simpson', 'Chunkylover53@aol.com',
                                      'Nuclear Technician', '.travis.yml'], input='Yes')
    assert not continue_result.exception
