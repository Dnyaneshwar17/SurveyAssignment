from pages.CreateSurvey import CreateSurvey
import unittest
import pytest
import utilities_config.custom_logger as cl
from utilities_config.Input import *
import logging

@pytest.mark.usefixtures("one_time_browser_setup")
class TestCreateSurvey(unittest.TestCase):
    log = cl.customLogger(logging.DEBUG)

    @pytest.fixture(autouse=True)
    def objectSetup(self, one_time_browser_setup):
        self.sc = CreateSurvey(one_time_browser_setup)

    @pytest.mark.run(order=1)
    def test_create_survey(self):
        print("start create survey")
        self.sc.start_create_survey(first_survey_name)
        result = self.sc.create_survey_successful()
        assert result == True

