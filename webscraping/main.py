from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
import os


WEBDRIVER_PATH = os.path.join(os.getcwd(), "webscraping", "chromedriver.exe")  

service = Service(WEBDRIVER_PATH)

def get_driver(target_url):
    options = webdriver.ChromeOptions()

    # ============== SET OPTIONS TO MAKE BROWSING EASIER ============

    # Disable showing bars with additional info.
    options.add_argument("disable-infobars")

    options.add_argument("start-maximized")

    # Avoiding issued when using Linux machine.
    options.add_argument("disable-dev-shm-usage")

    #Gives greater priviliges to browser.
    options.add_argument("no-sandbox")

    # Options that help Selenium avoid detection from the browser.
    options.add_experimental_option("excludeSwitches", ["enable-automation"])
    options.add_argument("disable-blink-features=AutomationControlled")

    # ============= OPTIONS ENDS =============

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

