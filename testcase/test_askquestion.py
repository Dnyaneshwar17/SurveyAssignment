from pages.AskQuestion import AskQuestion
import unittest
import pytest
import utilities_config.custom_logger as cl
from utilities_config.Input import*
import logging

@pytest.mark.usefixtures("start_survey")
class TestAskquestionSurvey(unittest.TestCase):
    log = cl.customLogger(logging.DEBUG)

    @pytest.fixture(autouse=True)
    def objectSetup(self, start_survey):
        self.question = AskQuestion(start_survey)

    @pytest.mark.run(order=4)
    def test_askquestion(self):
        print("start question on survey")
        self.question.first_question(first_question_enter)
        result = self.question.verify_question()
        assert result == True
