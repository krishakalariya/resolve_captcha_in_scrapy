# using anti-recaptcha
from python_anticaptcha import AnticaptchaClient, NoCaptchaTaskProxylessTask
from selenium import webdriver
import time

from selenium.webdriver.common.by import By

driver = webdriver.Chrome()


def captcha_solver():
    api_key = '41c6ae54404ffff6be997e0c5aba74d2'
    site_key = '6Le-wvkSAAAAAPBMRTvw0Q4Muexq9bi0DJwx_mJ-'  # grab from site
    url = 'https://www.google.com/recaptcha/api2/demo'

    client = AnticaptchaClient(api_key)
    task = NoCaptchaTaskProxylessTask(url, site_key)
    job = client.createTask(task)
    job.join()
    return job.get_solution_response()


captcha = captcha_solver()
driver.execute_script('document.getElementById("g-recaptcha-response").innerHTML = "{}";'.format(captcha))
time.sleep(1)
x = driver.find_element(By.XPATH, '//iframe[@title="reCAPTCHA"]')
submit = driver.find_element(By.CSS_SELECTOR, "button[type='submit']")
submit.click()
