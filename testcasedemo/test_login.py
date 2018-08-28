from pages.Login import Login
import unittest
import pytest
import utilities_config.custom_logger as cl
from utilities_config.Input import *
import logging

@pytest.mark.usefixtures("one_time_browser_setup")
class TestLoginDemo(unittest.TestCase):
    log = cl.customLogger(logging.DEBUG)

    @pytest.fixture(autouse=True)
    def objectSetup(self, one_time_browser_setup):
        self.login_start = Login(one_time_browser_setup)


    @pytest.mark.run(order=2)
    def test_validLogin(self):
        print("test_validLogin started")
        self.login_start.startlogin(username, password)
        result = self.login_start.login_successful()
        assert result == True