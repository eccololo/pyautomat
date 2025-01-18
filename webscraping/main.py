from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from settings import *
from utils import *
import time
import os
import datetime

HEADLESS = True

service = Service(WEBDRIVER_PATH)

def get_driver(target_url):
    options = set_driver_options(webdriver, HEADLESS)
    driver = webdriver.Chrome(service=service, options=options)
    driver.get(target_url)

    return driver

def get_aristotle_quote_from_target_website():
    driver = get_driver(TARGET_URL[0])
    element = driver.find_element(By.XPATH, "/html/body/div[1]/div/h1[1]")
    return element

def get_world_temperature_from_target_website():
    driver = get_driver(TARGET_URL[0])
    time.sleep(5)
    element = driver.find_element(By.XPATH, "/html/body/div[1]/div/h1[2]")
    return clean_world_temp_text(element.text)

def login_to_pythonhow_website_and_print_url():
    target_url = TARGET_URL[0]
    target_url = target_url + "/login"
    driver = get_driver(target_url)
    driver.find_element(By.ID, "id_username").send_keys(APP_USERNAME)
    time.sleep(2)
    driver.find_element(By.ID, "id_password").send_keys(PASSWORD + Keys.RETURN)
    time.sleep(5)
    driver.find_element(By.XPATH, "/html/body/nav/div/a").click()
    print(driver.current_url)

def login_to_pythonhow_and_get_dynamic_data():
    target_url = TARGET_URL[0]
    target_url = target_url + "/login"
    driver = get_driver(target_url)
    driver.find_element(By.ID, "id_username").send_keys(APP_USERNAME)
    time.sleep(2)
    driver.find_element(By.ID, "id_password").send_keys(PASSWORD + Keys.RETURN)
    time.sleep(5)
    element = driver.find_element(By.XPATH, "/html/body/div/h1[2]/div")
    return clean_world_temp_text(element.text)

def login_to_pythonhow_and_go_to_home_page():
    target_url = TARGET_URL[0]
    target_url = target_url + "/login"
    driver = get_driver(target_url)
    driver.find_element(By.ID, "id_username").send_keys(APP_USERNAME)
    time.sleep(2)
    driver.find_element(By.ID, "id_password").send_keys(PASSWORD + Keys.RETURN)
    time.sleep(5)
    return driver

def get_dynamic_data_from_pythonhow_homepage(driver):
    element = driver.find_element(By.XPATH, "/html/body/div/h1[2]/div")
    return clean_world_temp_text(element.text)

def write_text_to_file_with_timestamp(text):
    datetime_now = str(datetime.datetime.now().strftime("%d-%m-%Y_%H-%M-%S"))
    file_name = f"{datetime_now}.txt"
    file_path = os.path.join(os.getcwd(), "webscraping", file_name)  
    with open(file_path, "w") as f:
        f.write(text)

def save_dynamic_data_from_pythonhow_to_file(driver):
    dynamic_data = str(get_dynamic_data_from_pythonhow_homepage(driver))
    write_text_to_file_with_timestamp(dynamic_data)
  

if __name__ == "__main__":
    driver = login_to_pythonhow_and_go_to_home_page()
    for _ in range(120):
        time.sleep(2)
        save_dynamic_data_from_pythonhow_to_file(driver)