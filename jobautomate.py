import os
from indeed import IndeedClient
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, ElementNotVisibleException

driver = webdriver.Firefox()

with open('information.txt', 'r') as file:
    data = file.read().replace('\n', '').split(',')
    first_name, last_name, email_address, phone_number = data


def indeed_parameters(what, where):
    """Use Indeed API to obtain job application links.
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
              'fromage': 30,
              'start': 0,
              'userip': "1.2.3.4",
              'useragent': "Mozilla/5.0 (X11; Linux x86_64; rv:31.0) Gecko/20100101 Firefox/43.0"
              }
    return params


def indeed_urls(parameters):
    client = IndeedClient('7458209865285883')
    response = client.search(**parameters)
    urls = [str(links['url']) for links in response['results']]
    return urls


def switch_frames():
    """The job application is inside a nested frame. In order to navigate to
    the application, each frame must be selected."""
    wait = WebDriverWait(driver, 10)
    frame = wait.until(EC.presence_of_element_located(
        (By.CSS_SELECTOR, "iframe[name$=modal-iframe]")))
    driver.switch_to.frame(frame)
    driver.switch_to.frame(0)


def fill_application():
    """"""
    try:
        driver.find_element_by_id('applicant.name').send_keys("{} {}" .format(first_name, last_name))
        driver.find_element_by_id('applicant.email').send_keys(email_address)
        driver.find_element_by_id('applicant.phoneNumber').send_keys(phone_number)
        driver.find_element_by_id('resume').send_keys(os.path.abspath('resume.docx'))
        try:
            driver.find_element_by_link_text('Continue').click()
            driver.find_element_by_id('apply').click()
            print('Application Successful.')
        except ElementNotVisibleException:
            print('Application Failed.')
            driver.switch_to.window(driver.window_handles[0])

    except NoSuchElementException:
        driver.find_element_by_id('applicant.firstName').send_keys(first_name)
        driver.find_element_by_id('applicant.lastName').send_keys(last_name)
        driver.find_element_by_id('applicant.email').send_keys(email_address)
        driver.find_element_by_id('applicant.phoneNumber').send_keys(phone_number)
        driver.find_element_by_id('resume').send_keys(os.path.abspath('resume.docx'))
        try:
            driver.find_element_by_link_text('Continue').click()
            driver.find_element_by_id('apply').click()
            print('Application Successful.')
        except ElementNotVisibleException:
            print('Application Failed.')
            driver.switch_to.window(driver.window_handles[0])


def apply_to_job():
    """Click the Indeed apply button to easily apply to the job if it exists.
    If the application is identified as an Easily Apply job, the application
    is filled out. Otherwise, the new job window closes."""
    try:
        driver.find_element_by_class_name('indeed-apply-button').click()
        switch_frames()
        fill_application()
    except (NoSuchElementException, ElementNotVisibleException):
        pass


if __name__ == "__main__":
    user_parameters = indeed_parameters(raw_input('Enter a job title:'), raw_input('Enter a location:'))
    for url in indeed_urls(user_parameters):
        driver.get(url)
        apply_to_job()