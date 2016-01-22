"""
Title: Job Search Automation
Author: Mandeep Bhutani
Date: 01/05/2016

Description: This script when completed will hopefully assist those with the
dire need to apply for jobs.
"""
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException

job = input('Please enter a job:')
city = input('Please enter a city:')

driver = webdriver.Firefox()


def main():
    initiate_search()
    sort_results()
    click_job()
    switch_window()
    click_apply()
    switch_frames()
    fill_application()


def initiate_search():
    """Enter user input for job and city to begin a search."""
    driver.set_window_size(1024, 768)
    driver.get('https://www.indeed.com/')
    driver.find_element_by_name('q').send_keys(job)
    driver.find_element_by_id('where').clear()
    driver.find_element_by_id('where').send_keys(city)
    driver.find_element_by_id('fj').click()


def sort_results():
    """Sort the results by newest job first."""
    driver.find_element_by_link_text('date').click()


def click_job():
    """Click the link that redirects to the job application."""
    driver.find_element_by_xpath("//a[@data-tn-element='jobTitle']").click()


def switch_window():
    """Switch windows to the newly opened job application window."""
    driver.switch_to.window(driver.window_handles[1])


def click_apply():
    """Click the Indeed apply button to easily apply to the job.
    If the Indeed apply button does not exist, the new window closes."""
    try:
        driver.find_element_by_class_name('indeed-apply-button').click()
    except NoSuchElementException:
        driver.close()


def switch_frames():
    """The job application is inside a nested frame. In order to navigate to
    the appication, each frame must be selected."""
    wait = WebDriverWait(driver, 10)
    frame = wait.until(EC.presence_of_element_located(
        (By.CSS_SELECTOR, "iframe[name$=modal-iframe]")))
    driver.switch_to.frame(frame)
    driver.switch_to.frame(0)


def fill_application():
    """Submit the full name, email address, and resume of the job applicant.
    The function will assume that the full name is needed, however some applications
    will require a first name and last name."""
    try:
        driver.find_element_by_id('applicant.name').send_keys('Applicant Full Name')
        driver.find_element_by_id('applicant.email').send_keys('Email Address')
        driver.find_element_by_id('resume').send_keys('/home/usr/resume.doc')
        driver.find_element_by_id('applicant.applicationMessage').send_keys('Cover Letter')
        driver.find_element_by_link_text('Continue').click()
    except NoSuchElementException:
        driver.find_element_by_id('applicant.firstName').send_keys('Applicant First Name')
        driver.find_element_by_id('applicant.lastName').send_keys('Applicant Last Name')
        driver.find_element_by_id('applicant.email').send_keys('Email address')
        driver.find_element_by_id('applicant.phoneNumber').send_keys('123-456-7890')
        driver.find_element_by_id('resume').send_keys('/home/usr/resume.docx')
        driver.find_element_by_id('applicant.applicationMessage').send_keys('Cover Letter')
        driver.find_element_by_link_text('Continue').click()
        driver.find_element_by_id('apply').click()

if __name__ == "__main__":
    main()
