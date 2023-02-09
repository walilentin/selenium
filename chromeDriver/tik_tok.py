import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

from auth_data import vk_login, vk_password
from fake_useragent import UserAgent
import random


def tik_tok_auth(url):
    options = webdriver.ChromeOptions()
    options.add_argument(
        f"user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36")
    options.add_argument("--disable-blink-features=AutomationControlled")
    service = Service(executable_path='C:\\Users\\User\\PycharmProjects\\Selenium\\chromeDriver\\chromedriver')
    driver = webdriver.Chrome(service=service, options=options)

    try:
        driver.get(url=url)
        time.sleep(3)

        autho = driver.find_element(By.CLASS_NAME,'e13wiwn62').click()
        time.sleep(5)
    except Exception as ex:
        print(ex)
    finally:
        driver.close()
        driver.quit()
def main():
    tik_tok_auth("https://www.tiktok.com/uk-UA/")


if __name__ == '__main__':
    main()
