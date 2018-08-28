import pytest
from base.webdriver_factory import Browser_Factory
from pages.Login import Login
from utilities_config.Input import*

@pytest.yield_fixture(scope="class")
def one_time_browser_setup():
    get_driver = Browser_Factory(one_time_browser_setup)
    driver = get_driver.select_browser()
    log = Login(driver)
    log.startlogin(username, password)
    print("finished")
    return driver


#
