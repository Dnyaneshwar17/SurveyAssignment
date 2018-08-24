import pytest
from utilities_config.Input import*
from base.Browesr_factory import Browser_Factory
from pages.Login import Login
from pages.CreateSurvey import CreateSurvey
from pages.StartSurvey import StartSurvey
from pages.AskQuestion import AskQuestion

@pytest.fixture(scope='module')
def select_driver():
    select_driver = Browser_Factory("Chrome")
    driver = select_driver.select_browser()
    return driver

@pytest.mark.run(order=1)
def test_validLogin(select_driver):
    print("Valid Login Stared")
    lp = Login(select_driver)
    lp.startlogin(username, password)
    result = lp.login_successful()
    print("Result: " + str(result))

    assert result == True

@pytest.mark.run(order=2)
def test_create_survey(select_driver):
    print("create survey started")
    cs = CreateSurvey(select_driver)
    cs.start_create_survey(first_survey_name)
    result = cs.create_survey_successful()
    print("Result: " + str(result))

    assert result == True

@pytest.mark.run(order=3)
def test_survey_operation(select_driver):
    print("survey operation started")
    operation_survey = StartSurvey(select_driver)
    operation_survey.start_survey_operation(new_survey_title, new_page_title)
    result = operation_survey.surveyoperation_successful()
    print("Result: " + str(result))

    assert result == True



# @pytest.mark.run(order=6)
# def test_question_2(get_driver):
#     print("test_question_2 started")
#     survey_questions = SurveyQuestionPage(get_driver)
#     survey_questions.add_question_two(question_no_2)
#     result = survey_questions.verify_question()
#     print("Result: " + str(result))
#     assert result == True
#
# @pytest.mark.run(order=7)
# def test_question_3(get_driver):
#     print("test_question_3 started")
#     survey_questions = SurveyQuestionPage(get_driver)
#     survey_questions.add_question_three(question_no_3)
#     result = survey_questions.verify_question()
#     print("Result: " + str(result))
#     assert result == True
#
# @pytest.mark.run(order=8)
# def test_question_4(get_driver):
#     print("test_question_4 started")
#     survey_questions = SurveyQuestionPage(get_driver)
#     survey_questions.add_question_four(question_no_4)
#     result = survey_questions.verify_question()
#     print("Result: " + str(result))
#     assert result == True
#
# @pytest.mark.run(order=9)
# def test_question_5(get_driver):
#     print("test_question_5 started")
#     survey_questions = SurveyQuestionPage(get_driver)
#     survey_questions.add_question_five(question_no_5)
#     result = survey_questions.verify_question()
#     print("Result: " + str(result))
#     assert result == True
#









