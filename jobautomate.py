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

job = input('Please enter a job:')
city = input('Please enter a city:')

driver = webdriver.Firefox()


def initiate_search():
    """Enter user input job and city to begin a search."""
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
    links = driver.find_elements_by_xpath("//a[@data-tn-element='jobTitle']")
    for link in links:
        link.click()


def switch_window():
    """Switch windows to the newly opened job opening window."""
    driver.switch_to.window(driver.window_handles[1])


def apply_to_job():
    """Click the Indeed apply button to easily apply to the job.
    If the Indeed apply button does not exist, the new window closes."""
    try:
        driver.find_element_by_class_name('indeed-apply-button').click()
        wait = WebDriverWait(driver, 10)
        frame = wait.until(EC.presence_of_element_located(
            (By.CSS_SELECTOR, "iframe[name$=modal-iframe]")))
        driver.switch_to.frame(frame)
        driver.switch_to.frame(0)
        driver.find_element_by_id('applicant.name').send_keys('full name')
        driver.find_element_by_id('applicant.email').send_keys('email')
    except:
        driver.close()

if __name__ == "__main__":
    initiate_search()
    sort_results()
    click_job()
    while len(driver.window_handles) > 1:
        switch_window()
        apply_to_job()
