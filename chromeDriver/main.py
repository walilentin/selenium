# from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import time
import random
from fake_useragent import UserAgent
from seleniumwire import webdriver
from proxt_auth.auth import password, login

# url = 'https://www.instagram.com/'

proxy_options = {
    "proxy": {
        "https": f"https://{login}:{password}@138.128.91.65:8000"
    }

}
user_agents_list = [
    "hello_world",
    "best_of_the_best",
]

useragent = UserAgent()

# options
options = webdriver.ChromeOptions()

# add_arugument("user-agent=user-agent")

options.add_argument(f"user-agent={random.choice(user_agents_list)}")

# options.add_argument(f"user-agent={useragent.random}")

service = Service(executable_path='C:\\Users\\User\\PycharmProjects\\Selenium\\chromeDriver\\chromedriver')

# set proxy
# options.add_argument("--proxy-server=")

driver = webdriver.Chrome(service=service,options=options
                          )
# driver = webdriver.Chrome(service=service,
#                           seleniumwire_options=proxy_options)

try:
    # driver.get(url="https://vm.tiktok.com/ZMFFNJmLW")
    # time.sleep(5)

    driver.get("https://2ip.ru")
    driver.get_screenshot_as_file("1.png")
    time.sleep(5)



except Exception as ex:
    print(ex)
finally:
    driver.close()
    driver.quit()
