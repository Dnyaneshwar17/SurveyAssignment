from pages.Login import Login
import unittest
import pytest
import utilities_config.custom_logger as cl
from utilities_config.Input import *
import logging

@pytest.mark.usefixtures("get_driver")

class TestLoginDemo(unittest.TestCase):
    log = cl.customLogger(logging.DEBUG)

    @pytest.fixture(autouse=True)
    def objectSetup(self, select_browser):
        self.log = Login(select_browser)


    @pytest.mark.run(order=2)
    def test_validLogin(self):
        print("test_validLogin started")
        self.log.startlogin(username, password)
        result = self.log.login_successful()
        assert result == True