from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from settings import *
from utils import *



service = Service(WEBDRIVER_PATH)

def get_driver(target_url):
    options = set_driver_options(webdriver)
    driver = webdriver.Chrome(service=service, options=options)
    driver.get(target_url)

    return driver

def main():
    target_url = "http://automated.pythonanywhere.com"
    driver = get_driver(target_url)
    element = driver.find_element(By.XPATH, "/html/body/div[1]/div/h1[1]")
    return element



if __name__ == "__main__":
    print(main().text)

