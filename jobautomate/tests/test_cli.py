from click.testing import CliRunner
import jobautomate.commandline
import pytest


@pytest.fixture
def parameters():
    job_search = jobautomate.commandline.indeed_parameters('Financial Analyst', 'New York City')
    return job_search


@pytest.fixture
def application_one():
    """Returns a link with an application to test. This application combines the first name
    and last name in the same text box."""
    return "http://www.indeed.com/cmp/iCall-Services,-Inc./jobs/Sales-Professional-edfcb63f61b69c08"


@pytest.fixture
def application_two():
    """Returns a link with an application to test. This application contains a separate text
    box for first name and last name."""
    return "http://www.indeed.com/viewjob?jk=f6c24d6728d6b55f"


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


def test_indeed_apply_button(selenium, application_one):
    selenium.get(application_one)
    jobautomate.commandline.find_apply_button(selenium, 'indeed-apply-button')


def test_fill_application(selenium, application_one):
    selenium.get(application_one)
    fill(selenium)


def test_fill_application_again(selenium, application_two):
    selenium.get(application_two)
    fill(selenium)


def test_click_apply(selenium, application_one):
    selenium.get(application_one)
    fill(selenium)
    jobautomate.commandline.apply_or_continue(selenium, debug=True)


def test_click_apply_again(selenium, application_two):
    selenium.get(application_two)
    fill(selenium)
    jobautomate.commandline.apply_or_continue(selenium, debug=True)


def test_cli_command():
    runner = CliRunner(echo_stdin=True)
    result = runner.invoke(
        jobautomate.commandline.cli, ['--debug', 'Homer', 'Simpson', 'Chunkylover53@aol.com',
                                      'Nuclear Technician', '.travis.yml'], input='no')
    assert not result.exception


def test_cli_xvfb():
    runner = CliRunner(echo_stdin=True)
    xvfb_result = runner.invoke(
        jobautomate.commandline.cli, ['--debug', '--xvfb', 'Homer', 'Simpson',
                                      'Chunkylover53@aol.com', 'Nuclear Technician',
                                      '.travis.yml'], input='no')
    assert not xvfb_result.exception


def test_cli_verbose():
    runner = CliRunner(echo_stdin=True)
    verbose_result = runner.invoke(
        jobautomate.commandline.cli, ['--debug', '--verbose', 'Homer', 'Simpson',
                                      'Chunkylover53@aol.com', 'Nuclear Technician',
                                      '.travis.yml'], input='no')
    assert not verbose_result.exception


def test_cli_continue():
    runner = CliRunner(echo_stdin=True)
    continue_result = runner.invoke(
        jobautomate.commandline.cli, ['--debug', 'Homer', 'Simpson', 'Chunkylover53@aol.com',
                                      'Nuclear Technician', '.travis.yml'], input='no')
    assert not continue_result.exception
