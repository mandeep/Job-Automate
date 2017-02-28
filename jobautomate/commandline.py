import os

import click
from indeed import IndeedClient
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, ElementNotVisibleException
from xvfbwrapper import Xvfb


class InvalidAPIKey(Exception):
    """Raise when an invalid API key is supplied."""


def indeed_parameters(what, where):
    """Store parameters for use with the Indeed API.

    Positional arguments:
    what -- the description of the desired job
    where -- the location of the desired job

    :param q: job description
    :param l: job location; searches entire U.S. when left blank
    :param sort: sort results by relevance or date
    :param sr: direct hire only or include staffing agencies
    :param limit: number of results, 0-25
    :param fromage: number of days to search
    :param start: index of beginning search result
    :param userip: ip of client (required)
    :param useragent: user agent of client (required)
    """
    params = {'q': what,
              'l': where,
              'sort': 'date',
              'sr': 'directhire',
              'limit': 25,
              'fromage': 365,
              'start': 0,
              'userip': "1.2.3.4",
              'useragent': ("Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36"
                            "(KHTML, like Gecko) Chrome/48.0.2564.82 Safari/537.36")
              }
    return params


def access_indeed_api(parameters, publisher_key=None):
    """Access the Indeed API using the given parameters and publisher key.

    Positional argument:
    parameters -- a dictionary of the parameters to send to Indeed's API

    Keyword argument:
    publisher_key -- the publisher key for Indeed's API, defaults to environment variable
    """
    if publisher_key is None:
        publisher_key = os.environ['API_KEY']
    client = IndeedClient(publisher_key)
    response = client.search(**parameters)
    return response


def retrieve_indeed_urls(response):
    """Use the response from Indeed's API to retrieve job application URLs.

    Positional argument:
    response -- the HTTP response from Indeed's API
    """
    urls = [str(links['url']) for links in response['results']]
    return urls


def open_application(driver, button_name):
    """Search the job page for the Apply Now button and click it if it exists.

    Positional arguments:
    driver -- the Selenium webdriver instance
    button_name -- the class name of the button to click

    When the Apply Now button is clicked, the job application dialog
    opens in a new frame.
    """
    driver.implicitly_wait(1)
    driver.find_element_by_class_name(button_name).click()


def switch_frames(driver, frame_name):
    """Navigate nested iFrames to select the application modal dialog.

    Positional arguments:
    driver -- the Selenium webdriver instance
    frame_name -- the CSS selector of the frame to switch to
    """
    wait = WebDriverWait(driver, 15)
    frame = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, frame_name)))
    driver.switch_to.frame(frame)
    wait.until(EC.frame_to_be_available_and_switch_to_it(0))


def fill_application(driver, first_name, last_name, email, cv):
    """Fill the Indeed Easily Apply job application with the given arguments.

    Positional arguments:
    driver -- the Selenium webdriver instance
    first_name -- the first name to use on the job application
    last_name -- the last name to use on the job application
    email -- the email address to use on the job appication
    cv -- the file path of the resume to use on the job application
    """
    job_title = driver.find_element_by_class_name("jobtitle").text
    company = driver.find_element_by_class_name("jobcompany").text
    print("Applying for: {} at {}".format(job_title, company))
    driver.find_element_by_id('applicant.name').send_keys("{} {}" .format(first_name, last_name))
    driver.find_element_by_id('applicant.email').send_keys(email)
    driver.find_element_by_id('resume').send_keys(os.path.abspath(cv))


def submit_application(driver, debug=False):
    """Click the apply button and submit the application.

    Positional argument:
    driver -- the Selenium webdriver instance

    Keyword argument:
    debug -- flag used for testing to omit application submission

    There are two types of apply methods: one applies after
    clicking the apply button, and the other applies after clicking the
    continue button and answering some questions. The try/except clause
    clicks the apply button if it exists, otherwise it will click the continue
    button and select the radio buttons that indicate 'Yes'.
    """
    try:
        driver.find_element_by_link_text('Continue').click()
        driver.implicitly_wait(1)
        for radio_button in driver.find_elements_by_xpath('//*[@type="radio" and @value="0"]'):
            radio_button.click()
        if not debug:
            driver.find_element_by_id('apply').click()
        driver.implicitly_wait(1)
        print('Application Successful.')
    except (NoSuchElementException, ElementNotVisibleException):
        if not debug:
            driver.find_element_by_id('apply').click()
        driver.implicitly_wait(1)
        print('Application Successful.')
    finally:
        driver.switch_to.window(driver.window_handles[0])


@click.command()
@click.option('--debug', is_flag=True,
              help="Disable click on apply button found on job applications.")
@click.option('--key', default=None, help="Indeed Publisher ID")
@click.option('--xvfb', is_flag=True, help="Run the application in a headless browser.")
@click.option('--verbose', is_flag=True,
              help="Print to standard output the jobs that are not easily apply applications.")
@click.argument('first_name')
@click.argument('last_name')
@click.argument('email_address')
@click.argument('job_description')
@click.argument('resume', type=click.Path(exists=True))
@click.argument('job_location', default='')
def cli(debug, key, xvfb, verbose, first_name, last_name, email_address,
        job_description, resume, job_location):
    """Apply to jobs automatically with Job Automate.

    Job Automate requires the user's first name, last name, email address, job description,
    and resume location prior to automating a job search. The job location is an optional argument
    that is left blank by default. This allows Job Automate to search for jobs across the
    entire United States. Each of the command line arguments requires a string data type. In
    order to pass a string to each argument, type each argument inside quotation marks.

    An example usage: jobautomate --key ABC123 "Homer" "Simpson" "Chunkylover53@aol.com"
    "Nuclear Technician" "/path/to/resume.txt" "Springfield"

    When run, jobautomate will print to terminal the job position and company name tied to
    the easily apply application. With the --verbose flag, jobautomate will also print to
    terminal the applications which are not easily apply applications.
    """
    if xvfb:
        vdisplay = Xvfb()
        vdisplay.start()

    user_parameters = indeed_parameters(job_description, job_location)
    response = access_indeed_api(user_parameters, key)

    if response == {'error': 'Invalid publisher number provided.'}:
        raise InvalidAPIKey(response)

    driver = webdriver.Firefox()
    while True:
        for url in retrieve_indeed_urls(response):
            driver.get(url)
            try:
                open_application(driver, 'indeed-apply-button')
                switch_frames(driver, 'iframe[name$=modal-iframe]')
                fill_application(driver, first_name, last_name, email_address, resume)
                if debug:
                    submit_application(driver, debug=True)
                else:
                    submit_application(driver)
            except (NoSuchElementException, ElementNotVisibleException):
                if verbose:
                    print('Not an easily apply job application.')
                else:
                    pass

        user_prompt = click.prompt('Would you like to continue searching for jobs? (yes/no)')
        if user_prompt == 'yes':
            user_parameters['start'] += 25
            response = access_indeed_api(user_parameters, key)
        else:
            driver.quit()
            if xvfb:
                vdisplay.stop()
            break
