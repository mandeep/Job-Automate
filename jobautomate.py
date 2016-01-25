import os
from indeed import IndeedClient
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, ElementNotVisibleException


def indeed_search():
    """Use Indeed API to obtain job application links.
    :param q: job description
    :param l: job location
    :param sort: sort results by relevance or date
    :param sr: direct hire only or include staffing agencies
    :param limit: number of results, 0-25
    :param fromage: number of days to search
    :param start: index of beginning search result
    :param userip: ip of client (required)
    :param useragent: user agent of client (required)
    """
    client = IndeedClient('7458209865285883')

    params = {'q': 'analyst',
              'l': "",
              'sort': 'date',
              'sr': 'directhire',
              'limit': 25,
              'fromage': 30,
              'start': 0,
              'userip': "1.2.3.4",
              'useragent': "Mozilla/5.0 (X11; Linux x86_64; rv:31.0) Gecko/20100101 Firefox/43.0"
              }

    response = client.search(**params)
    urls = [str(links['url']) for links in response['results']]
    return urls

driver = webdriver.Firefox()

with open('information.txt', 'r') as file:
    data = file.read().replace('\n', '').split(',')
    first_name, last_name, email_address, phone_number = data


def main_window():
    driver.switch_to.window(driver.window_handles[0])


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
            driver.find_element_by_id('apply').click()
            print('Application Successful.')
        except ElementNotVisibleException:
            driver.close()
            print('Application Failed.')
            main_window()

    except NoSuchElementException:
        driver.find_element_by_id('applicant.firstName').send_keys(first_name)
        driver.find_element_by_id('applicant.lastName').send_keys(last_name)
        driver.find_element_by_id('applicant.email').send_keys(email_address)
        driver.find_element_by_id('applicant.phoneNumber').send_keys(phone_number)
        driver.find_element_by_id('resume').send_keys(os.path.abspath('resume.docx'))
        try:
            driver.find_element_by_id('apply').click()
            print('Application Successful.')
        except ElementNotVisibleException:
            driver.close()
            print('Application Failed.')
            main_window()


def click_apply():
    """Click the Indeed apply button to easily apply to the job if it exists.
    If the application is identified as an Easily Apply job, the application
    is filled out. Otherwise, the new job window closes."""
    try:
        driver.find_element_by_class_name('indeed-apply-button').click()
        switch_frames()
        fill_application()
        main_window()
    except (NoSuchElementException, ElementNotVisibleException):
        driver.close()
        main_window()


if __name__ == "__main__": pass