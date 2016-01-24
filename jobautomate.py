from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, ElementNotVisibleException

job = input('Please enter a job:')
city = input('Please enter a city:')

driver = webdriver.Firefox()

with open('information.txt', 'r') as file:
    data = file.read().replace('\n', '').split(',')
    first_name, last_name, email_address, phone_number = data


def initiate_search():
    """Enter user input for job and city to begin an Indeed search."""
    driver.set_window_size(1024, 768)
    driver.get('https://www.indeed.com/')
    driver.find_element_by_name('q').send_keys(job)
    driver.find_element_by_id('where').clear()
    driver.find_element_by_id('where').send_keys(city)
    driver.find_element_by_id('fj').click()
    try:
        driver.find_element_by_id('prime-popover-close-button').click()
    except:
        pass


def sort_results():
    """Sort the results by newest job first."""
    driver.find_element_by_link_text('date').click()


def click_job():
    """Click the link that redirects to the job application."""
    return driver.find_elements_by_xpath("//a[@data-tn-element='jobTitle']")


def switch_window():
    """Switch windows to the newly opened job application window."""
    driver.switch_to.window(driver.window_handles[1])


def switch_frames():
    """The job application is inside a nested frame. In order to navigate to
    the application, each frame must be selected."""
    wait = WebDriverWait(driver, 10)
    frame = wait.until(EC.presence_of_element_located(
        (By.CSS_SELECTOR, "iframe[name$=modal-iframe]")))
    driver.switch_to.frame(frame)
    driver.switch_to.frame(0)


def fill_application():
    """Indeed gives employers four applications to choose from. The function
    uses try/except to identify the application Some fields are not required; 
    however, they are filled out just in case."""
    try:
        driver.find_element_by_id('applicant.name').send_keys(first_name + " " + last_name)
        driver.find_element_by_id('applicant.email').send_keys(email_address)
        driver.find_element_by_id('applicant.phoneNumber').send_keys(phone_number)
        driver.find_element_by_id('resume').send_keys('/home/mandeep/Desktop/resume.docx')
        try:
            driver.find_element_by_id('apply').click()
        except ElementNotVisibleException:
            driver.find_element_by_link_text('Continue').click()
            driver.find_element_by_id('apply').click()
        else:
            driver.close()
    except NoSuchElementException:
        driver.find_element_by_id('applicant.firstName').send_keys(first_name)
        driver.find_element_by_id('applicant.lastName').send_keys(last_name)
        driver.find_element_by_id('applicant.email').send_keys(email_address)
        driver.find_element_by_id('applicant.phoneNumber').send_keys(phone_number)
        driver.find_element_by_id('resume').send_keys('/home/mandeep/Desktop/resume.docx').submit()
        try:
            driver.find_element_by_id('apply').click()
        except ElementNotVisibleException:
            driver.find_element_by_link_text('Continue').click()
            driver.find_element_by_id('apply').click()
        else:
            driver.close()


def click_apply():
    """Click the Indeed apply button to easily apply to the job if it exists.
    If the application is identified as an Easily Apply job, the application
    is filled out. Otherwise, the new job window closes."""
    try:
        driver.find_element_by_class_name('indeed-apply-button').click()
        switch_frames()
        fill_application()
    except NoSuchElementException:
        driver.close()
        driver.switch_to.window(driver.window_handles[0])


if __name__ == "__main__":
    initiate_search()
    sort_results()
    for link in click_job():
        link.click()
        switch_window()
        click_apply()
