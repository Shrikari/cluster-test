import pytest
from selenium.webdriver import Firefox, Chrome, Ie
def get_driver_instance():
    browser_type = pytest.config.option.type.lower()
    env = pytest.config.option.env.lower()
    if env == 'local':
        if browser_type == 'firefox':
            driver = Firefox('./browser_servers/geckodriver.exe')
        elif browser_type == 'chrome':
            driver = Chrome('./browser_servers/chromedriver.exe')
        else:
            print('Invalid Browser Option')
    elif env == 'remote':
        print('Add features for remote execution')
    else:
        print('Invalid Env option')
    driver.maximize_window()
    driver.implicitly_wait(30)
    driver.get('http://localhost')
    return driver

