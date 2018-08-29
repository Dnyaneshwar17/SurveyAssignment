from pages.StartSurvey import StartSurvey
import unittest
import pytest
import utilities_config.custom_logger as cl
from utilities_config.Input import *
import logging

@pytest.mark.usefixtures("start_survey")
class TestStartSurvey(unittest.TestCase):
    log = cl.customLogger(logging.DEBUG)

    @pytest.fixture(autouse=True)
    def objectSetup(self, start_survey):
        self.ss = StartSurvey(start_survey)

    @pytest.mark.run(order=3)
    def test_start_survey(self):
        print("start survey creation")
        self.ss.start_survey_operation(new_survey_title, new_page_title)
        result = self.ss.surveyoperation_successful()
        assert result == True
