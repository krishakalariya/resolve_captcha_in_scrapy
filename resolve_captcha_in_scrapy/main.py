# using selenium-recaptcha-solver
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium_recaptcha_solver import RecaptchaSolver
from selenium.webdriver.chrome.options import Options
import time
test_ua = 'Mozilla/5.0 (Windows NT 4.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/37.0.2049.0 Safari/537.36'

options = Options()

options.add_argument("--headless")  # Remove this if you want to see the browser (Headless makes the chromedriver not have a GUI)
options.add_argument("--window-size=1920,1080")

options.add_argument(f'--user-agent={test_ua}')

options.add_argument('--no-sandbox')
options.add_argument("--disable-extensions")
driver = webdriver.Chrome()
web_url = "https://www.google.com/recaptcha/api2/demo"
solver = RecaptchaSolver(driver=driver)
driver.get(web_url)
recaptcha_iframe = driver.find_element(By.XPATH, '//iframe[@title="reCAPTCHA"]')
print('recaptcha_iframe')
time.sleep(4)
solver.click_recaptcha_v2(iframe=recaptcha_iframe)
submit = driver.find_element(By.CSS_SELECTOR, "input[type='submit']")
submit.click()
