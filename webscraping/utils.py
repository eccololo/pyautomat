def set_driver_options(webdriver):
    options = webdriver.ChromeOptions()

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
    
    return options

def clean_world_temp_text(text):
    """This function cleans text of world temperature taken from website."""
    return float(text.split(": ")[1])