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

user_agents_list = [
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36',

]

useragent = UserAgent()
options = webdriver.ChromeOptions()

options.add_argument(
    f"user-agent=Mozilla/5.0 (Macintosh; Intel Mac OS X 12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36")

service = Service(executable_path='C:\\Users\\User\\PycharmProjects\\Selenium\\chromeDriver\\chromedriver')

driver = webdriver.Chrome(service=service, options=options)
try:
    driver.get(url="https://vk.com/")
    time.sleep(3)
    email_input = driver.find_element(By.ID, 'index_email')
    email_input.clear()
    email_input.send_keys(vk_login)
    email_input.send_keys(Keys.ENTER)


    time.sleep(5)
    password_input = driver.find_element(By.NAME, 'password')
    password_input.clear()
    password_input.send_keys(vk_password)
    password_input.send_keys(Keys.ENTER)

    time.sleep(5)

    enter_news = driver.find_element(By.LINK_TEXT, 'Моя страница').click()
    time.sleep(5)


except Exception as ex:
    print(ex)
finally:
    driver.close()
    driver.quit()
