# using 2captcha
from selenium import webdriver
import requests
import time

driver = webdriver.Chrome()
web_url = "https://www.google.com/recaptcha/api2/demo"
driver.get(web_url)

api_key = "49378381dfefc28d2929d6996b2f63ae"
site_key = "6Le-wvkSAAAAAPBMRTvw0Q4Muexq9bi0DJwx_mJ-"

form = {"method": "userrecaptcha",
        "googlekey": site_key,
        "key": api_key,
        "pageurl": web_url,
        "json": 1}

response = requests.post('http://2captcha.com/in.php', data=form)
request_id = response.json()['request']

url = f"http://2captcha.com/res.php?key={api_key}&action=get&id={request_id}&json=1"

status = 0
while not status:
    res = requests.get(url)
    if res.json()['status'] == 0:
        time.sleep(3)
    else:
        request = res.json()['request']
        captcha = f'document.getElementById("g-recaptcha-response").innerHTML="{request}";'
        driver.execute_script(captcha)
        driver.find_element("id", 'recaptcha-demo-submit').submit()
        status = 1
