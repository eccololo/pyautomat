from decouple import config
import os


WEBDRIVER_PATH = os.path.join(os.getcwd(), "webscraping", "chromedriver.exe")  
TARGET_URL = ["http://automated.pythonanywhere.com", "https://finance.yahoo.com/"]
APP_USERNAME = config("APP_USERNAME")
PASSWORD = config("PASSWORD")