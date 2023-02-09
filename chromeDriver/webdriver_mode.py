# from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import time
import random
from fake_useragent import UserAgent
from seleniumwire import webdriver
from proxt_auth.auth import password, login
from selenium.webdriver.common.by import By
from auth_data import *
from selenium.webdriver.common.keys import Keys
import pickle

user_agents_list = [
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36',

]

useragent = UserAgent()
options = webdriver.ChromeOptions()


options.add_argument(
    f"user-agent=Mozilla/5.0 (Macintosh; Intel Mac OS X 12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36")

# disavle webdriver mode

# for older ChromeDriver under  version 79.0.3945.16
# options.add_experimental_option("excludeSwitchers", ["enable-automation"])
# options.add_experimental_option("useAutomationExtension", False)

# for new ChromeDriver version
options.add_argument("--disable-blink-features=AutomationControlled")
service = Service(executable_path='C:\\Users\\User\\PycharmProjects\\Selenium\\chromeDriver\\chromedriver')
driver = webdriver.Chrome(service=service, options=options)
try:
    driver.get(url="https://bot.sannysoft.com/")
    time.sleep(5)
except Exception as ex:
    print(ex)
finally:
    driver.close()
    driver.quit()
