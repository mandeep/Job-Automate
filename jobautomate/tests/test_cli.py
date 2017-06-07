from click.testing import CliRunner
import pytest

import jobautomate.commandline


@pytest.fixture
def parameters():
    """Store the parameters for use with the Indeed API."""
    job_search = jobautomate.commandline.indeed_parameters('Financial Analyst', 'New York City')
    return job_search


@pytest.fixture
def application():
    """Link to a working job application."""
    return ('https://www.indeed.com/viewjob?jk=057f0c06ba15ff48')


def fill(driver):
    """Open and fill an easily apply application."""
    jobautomate.commandline.open_application(driver, 'indeed-apply-button')
    jobautomate.commandline.switch_frames(driver, 'iframe[name$=modal-iframe]')
    jobautomate.commandline.fill_application(
        driver, 'Homer', 'Simpson', 'Chunkylover53@aol.com', 'resume.txt')


def test_indeed_api_parameters(parameters):
    """Test that the Indeed API returns the correct values."""
    assert isinstance(parameters, dict) is True
    assert 'Financial Analyst' in parameters.values()
    assert 'New York City' in parameters.values()


def test_retrieve_indeed_urls(selenium, parameters):
    """Test that the Indeed API returns 25 job application URLs."""
    response = jobautomate.commandline.access_indeed_api(parameters)
    job_urls = jobautomate.commandline.retrieve_indeed_urls(response)
    assert len(job_urls) == 25
    assert all('http://' in url for url in job_urls)


def test_false_api_key(parameters):
    """Test that an invalid API key returns an error."""
    assert jobautomate.commandline.access_indeed_api(
        parameters,
        123456789) == {'error': 'Invalid publisher number provided.'}


def test_open_application(selenium, application):
    """Test that an easily apply application opens properly."""
    selenium.get(application)
    jobautomate.commandline.open_application(selenium, 'indeed-apply-button')


def test_fill_application(selenium, application):
    """Test that an easily apply application can be filled."""
    selenium.get(application)
    fill(selenium)


def test_application_submission(selenium, application):
    """Test that all steps up to submitting the application are completed."""
    selenium.get(application)
    fill(selenium)
    jobautomate.commandline.submit_application(selenium, debug=True)


def test_cli_command():
    """Test the CLI."""
    runner = CliRunner(echo_stdin=True)
    result = runner.invoke(
        jobautomate.commandline.cli, ['--debug', 'Homer', 'Simpson', 'Chunkylover53@aol.com',
                                      'Nuclear Technician', '.travis.yml'], input='no')
    assert not result.exception


def test_cli_false_key():
    """Test the CLI with a false API key."""
    runner = CliRunner(echo_stdin=True)
    result = runner.invoke(
        jobautomate.commandline.cli, ['--debug', '--key', 'FALSEAPIKEY', 'Homer', 'Simpson',
                                      'Chunkylover53@aol.com', 'Nuclear Technician',
                                      '.travis.yml'], input='no')
    assert result.exception


def test_cli_xvfb():
    """Test the CLI with the --xvfb flag."""
    runner = CliRunner(echo_stdin=True)
    xvfb_result = runner.invoke(
        jobautomate.commandline.cli, ['--debug', '--xvfb', 'Homer', 'Simpson',
                                      'Chunkylover53@aol.com', 'Nuclear Technician',
                                      '.travis.yml'], input='no')
    assert not xvfb_result.exception


def test_cli_verbose():
    """Test the CLI with the --verbose flag."""
    runner = CliRunner(echo_stdin=True)
    verbose_result = runner.invoke(
        jobautomate.commandline.cli, ['--debug', '--verbose', 'Homer', 'Simpson',
                                      'Chunkylover53@aol.com', 'Nuclear Technician',
                                      '.travis.yml'], input='no')
    assert not verbose_result.exception
