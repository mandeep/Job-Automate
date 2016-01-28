import os
from indeed import IndeedClient
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, ElementNotVisibleException

driver = webdriver.Firefox()
driver.set_window_size(1024, 768)

with open('information.txt', 'r') as file:
    data = file.read().replace('\n', '').split(',')
    first_name, last_name, email_address = data


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
              'fromage': 90,
              'start': 0,
              'userip': "1.2.3.4",
              'useragent': "Mozilla/5.0 (X11; Linux x86_64; rv:31.0) Gecko/20100101 Firefox/43.0"
              }
    return params


def indeed_urls(parameters):
    """Use Indeed publisher ID in order to gain access to the API. With
    parameters from indeed_paramters(), return a list of job application links."""
    client = IndeedClient('7458209865285883')
    response = client.search(**parameters)
    urls = [str(links['url']) for links in response['results']]
    return urls


def switch_frames(frame_name):
    """The job application is inside a nested frame. In order to navigate to
    the application, each frame must be selected."""
    wait = WebDriverWait(driver, 10)
    frame = wait.until(EC.presence_of_element_located(
        (By.CSS_SELECTOR, frame_name)))
    driver.switch_to.frame(frame)
    driver.switch_to.frame(0)


def fill_application(cv_resume):
    """There are two application types: one that requires a full name and one
    that requires a first and last name. A try/except is used to identify which
    is used. Then, there are two types of apply methods. One applies after
    clicking the apply button, and the other applies after clicking the
    continue button and then answering some questions. A try/except is used
    again here to identify which is used."""
    try:
        driver.find_element_by_id('applicant.name').send_keys("{} {}" .format(first_name, last_name))
        driver.find_element_by_id('applicant.email').send_keys(email_address)
        driver.find_element_by_id('resume').send_keys(os.path.abspath(cv_resume))
        try:
            driver.find_element_by_link_text('Continue').click()
            for radio_button in driver.find_elements_by_xpath('//*[@type="radio" and @value="0"]'):
                radio_button.click()
            driver.find_element_by_id('apply').click()
            print('Application Successful.')
        except (ElementNotVisibleException, NoSuchElementException):
            driver.find_element_by_id('apply').click()
            print('Application Successful.')
        else:
            driver.switch_to.window(driver.window_handles[0])
    except (NoSuchElementException, ElementNotVisibleException):
        driver.find_element_by_id('applicant.firstName').send_keys(first_name)
        driver.find_element_by_id('applicant.lastName').send_keys(last_name)
        driver.find_element_by_id('applicant.email').send_keys(email_address)
        driver.find_element_by_id('resume').send_keys(os.path.abspath(cv_resume))
        try:
            driver.find_element_by_link_text('Continue').click()
            for radio_button in driver.find_element_by_xpath('//*[@type="radio" and @value="0"]'):
                radio_button.click()
            driver.find_element_by_id('apply').click()
            print('Application Successful.')
        except (ElementNotVisibleException, NoSuchElementException):
            driver.find_element_by_id('apply').click()
            print('Application Successful.')
        else:
            driver.switch_to.window(driver.window_handles[0])


def main():
    user_parameters = indeed_parameters(raw_input('Enter a job title:'), raw_input('Enter a location:'))
    count = 0
    while count < 40:
        for url in indeed_urls(user_parameters):
            driver.get(url)
            try:
                driver.find_element_by_class_name('indeed-apply-button').click()
                switch_frames('iframe[name$=modal-iframe]')
                fill_application('resume.docx')
            except (NoSuchElementException, ElementNotVisibleException):
                print('Not an easily apply application.')
        user_parameters['start'] += 25
        count += 1
