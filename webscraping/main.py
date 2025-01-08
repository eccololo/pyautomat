from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from settings import *
from utils import *
import time
import os


service = Service(WEBDRIVER_PATH)

def get_driver(target_url):
    options = set_driver_options(webdriver)
    driver = webdriver.Chrome(service=service, options=options)
    driver.get(target_url)

    return driver

def get_aristotle_quote_from_target_website():
    driver = get_driver(TARGET_URL)
    element = driver.find_element(By.XPATH, "/html/body/div[1]/div/h1[1]")
    return element

def get_world_temperature_from_target_website():
    driver = get_driver(TARGET_URL)
    time.sleep(5)
    element = driver.find_element(By.XPATH, "/html/body/div[1]/div/h1[2]")
    return clean_world_temp_text(element.text)

def login_to_pythonhow_website_and_print_url():
    target_url = TARGET_URL
    target_url = target_url + "/login"
    driver = get_driver(target_url)
    driver.find_element(By.ID, "id_username").send_keys(APP_USERNAME)
    time.sleep(2)
    driver.find_element(By.ID, "id_password").send_keys(PASSWORD + Keys.RETURN)
    time.sleep(5)
    driver.find_element(By.XPATH, "/html/body/nav/div/a").click()
    print(driver.current_url)


if __name__ == "__main__":
    login_to_pythonhow_website_and_print_url()