import pytest
from base.Browesr_factory import Browser_Factory
from pages.Login import Login
from utilities_config.Input import*

@pytest.yield_fixture(scope="class")

def select_browser():
    get_driver = Browser_Factory()
    driver = get_driver.select_browser()
    log = Login(driver)
    log.startlogin(username,password)
    print("end of get_driver")
    return driver
