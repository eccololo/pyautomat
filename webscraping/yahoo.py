from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from settings import *
from utils import *
import time

# Apple - APPL
# Microsoft - MSFT

HEADLESS = False

service = Service(WEBDRIVER_PATH)

def get_driver(target_url):
    options = set_driver_options(webdriver, HEADLESS)
    driver = webdriver.Chrome(service=service, options=options)
    driver.get(target_url)

    return driver

# 
def get_stock_data_from_last_year(stock_id):
    headers = ["Date", "Open", "High", "Low", "Close", "Adj Close", "Volume"]
    driver = get_driver(TARGET_URL[1])
    time.sleep(4)
    driver.find_element(By.XPATH, "/html/body/div/div/div/div/form/div[2]/div[2]/button[1]").click()
    time.sleep(4)
    driver.find_element(By.ID, "ybar-sbq").send_keys(stock_id + Keys.RETURN)
    time.sleep(4)
    driver.find_element(By.XPATH, "/html/body/div[2]/main/section/section/aside/section/nav/ul/li[6]/a").click()
    time.sleep(4)


if __name__ == "__main__":
    get_stock_data_from_last_year("APPL")