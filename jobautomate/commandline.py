import click

from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException, ElementNotVisibleException

from xvfbwrapper import Xvfb

from jobautomate import jobautomate


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

    user_parameters = jobautomate.indeed_parameters(job_description, job_location)
    response = jobautomate.access_indeed_api(user_parameters, key)

    if response == {'error': 'Invalid publisher number provided.'}:
        raise jobautomate.InvalidAPIKey(response)

    driver = webdriver.Firefox()
    while True:
        for url in jobautomate.retrieve_indeed_urls(response):
            driver.get(url)
            try:
                jobautomate.open_application(driver, 'indeed-apply-button')
                jobautomate.switch_frames(driver, 'iframe[name$=modal-iframe]')
                jobautomate.fill_application(driver, first_name, last_name, email_address, resume)
                if debug:
                    jobautomate.submit_application(driver, debug=True)
                else:
                    jobautomate.submit_application(driver)
            except (NoSuchElementException, ElementNotVisibleException):
                if verbose:
                    print('Not an easily apply job application.')
                else:
                    pass

        user_prompt = click.prompt('Would you like to continue searching for jobs? (yes/no)')
        if user_prompt == 'yes':
            user_parameters['start'] += 25
            response = jobautomate.access_indeed_api(user_parameters, key)
        else:
            driver.quit()
            if xvfb:
                vdisplay.stop()
            break
