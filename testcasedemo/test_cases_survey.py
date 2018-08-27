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


@pytest.mark.run(order=4)
def test_question_first(select_driver):
    print("first question ")
    questions_first = AskQuestion(select_driver)
    questions_first.first_question(first_question_enter)
    result = questions_first.verify_question()
    print("Result: " + str(result))

    assert result == True

@pytest.mark.run(order=5)
def test_question_2(select_driver):
    print("second question ")
    questions_second = AskQuestion(select_driver)
    questions_second.second_question(second_question_enter)
    result = questions_second.verify_question()
    print("Result: " + str(result))
    assert result == True

@pytest.mark.run(order=6)
def test_question_4(select_driver):
    print("four question")
    questions_four = AskQuestion(select_driver)
    questions_four.four_question(four_question_enter)
    result = questions_four.verify_question()
    print("Result: " + str(result))
    assert result == True


@pytest.mark.run(order=7)
def test_question_10(select_driver):
    print("ten question")
    questions_ten = AskQuestion(select_driver)
    questions_ten.ten_question(ten_question_enter)
    result = questions_ten.verify_question()
    print("Result: " + str(result))
    assert result == True



@pytest.mark.run(order=8)
def test_question_3(select_driver):
    print("third question")
    questions_third = AskQuestion(select_driver)
    questions_third.third_question(third_question_enter)
    result = questions_third.verify_question()
    print("Result: " + str(result))
    assert result == True

@pytest.mark.run(order=9)
def test_question_5(select_driver):
    print("five question")
    questions_five = AskQuestion(select_driver)
    questions_five.five_question(five_question_enter)
    result = questions_five.verify_question()
    print("Result: " + str(result))
    assert result == True

@pytest.mark.run(order=10)
def test_question_9(select_driver):
    print(" nine question ")
    questions_nine = AskQuestion(select_driver)
    questions_nine.nine_question(nine_question_enter)
    result = questions_nine.verify_question()
    print("Result: " + str(result))
    assert result == True

# @pytest.mark.run(order=10)
# def test_question_6(select_driver):
#         print(" six question ")
#         questions_six = AskQuestion(select_driver)
#         questions_six.six_question(six_question_enter)
#         result = questions_six.verify_question()
#         print("Result: " + str(result))
#         assert result == True
#
