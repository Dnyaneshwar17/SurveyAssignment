from base.basepage import BasePage
from utilities_config.Input import*
import time

class AskQuestion(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    _enter_question = "editTitle"
    _enter_question_type = "changeQType"
    _question_save_button = "//div[@id='editQuestion']/section[@class='t1']//a[text()='SAVE']"
    _add_new_question = "//a[.='NEW QUESTION']"
    _survey_body = "create"

    first_question_pattern = "//ul[@class='add-q-menu-left']//a[text()='Single Textbox']"

      # Second Question:
    second_question_pattern = "//ul[@class='add-q-menu-right']//a[text()='Date / Time']"
    second_question_select_pattern = "//table[@id='rows']/tfoot[@class='answerTableFooter']//label[.='Time Info']"

      # Third Question:

    third_nine_question_pattern = "//ul[@class='add-q-menu-left']//a[text()='Multiple Choice']"
    third_nine_question_select_pattern = "//div[@id='editQuestion']//select[@id='answerBankCategorySelect']"
    third_question_select_specific = "//option[contains(text(),'Always - Never')]"


      # Four Question:
    four_question_pattern = "//ul[@class='add-q-menu-left']//a[text()='Star Rating']"

      # Five Question:
    five_question_pattern = "//ul[@class='add-q-menu-right']//a[text()='Dropdown']"
    five_nine_question_select_specific = "//option[contains(text(),'Yes - No')]"

    #Six Question:
    six_question_pattern = "//ul[@class='add-q-menu-left']//a[text()='Checkboxes']"
    six_question_1 = "//table[@id='rows']/tbody[@class='answerSetting singleLine']/tr[4]/td[2]/div/div[1]"
    six_question_2 = "//table[@id='rows']/tbody[@class='answerSetting singleLine']/tr[5]/td[2]/div/div[1]"
    six_question_3 = "//table[@id='rows']/tbody[@class='answerSetting singleLine']/tr[6]/td[2]/div/div[1]"
    six_question_4 = "//table[@id='rows']/tbody[@class='answerSetting singleLine']/tr[7]/td[2]/div/div[1]"
    six_question_5 = "//table[@id='rows']/tbody[@class='answerSetting singleLine']/tr[8]/td[2]/div/div[1]"

    # seven question
    seven_question_pattern = "//ul[@class='add-q-menu-right']//a[text()='Matrix / Rating Scale']"
    seven_question_1 = "//table[@id='rows']/tbody[@class='answerSettingMatrix singleLine']/tr[3]/td[1]/div/div[1]"
    seven_question_2 = "//table[@id='rows']/tbody[@class='answerSettingMatrix singleLine']/tr[4]/td[1]/div/div[1]"
    seven_question_3 = "//table[@id='rows']/tbody[@class='answerSettingMatrix singleLine']/tr[5]/td[1]/div/div[1]"
    seven_question_4 = "//div[@id='columnsWrap']//table/tbody[@class='columnSetting singleLine']/tr[2]/td[1]/div/div[1]"
    seven_question_5 = "//div[@id='columnsWrap']//table/tbody[@class='columnSetting singleLine']/tr[3]/td[1]/div/div[1]"
    seven_question_6 = "//div[@id='columnsWrap']//table/tbody[@class='columnSetting singleLine']/tr[4]/td[1]/div/div[1]"
    seven_question_7 = "//div[@id='columnsWrap']//table/tbody[@class='columnSetting singleLine']/tr[5]/td[1]/div/div[1]"

    #Eight Question
    eight_question_pattern="//ul[@class='add-q-menu-right']//a[text()='Multiple Textboxes']"
    eight_question_1 = "//table[@id='rows']/tbody[@class='answerSettingTextboxes']/tr[3]/td[1]/div/div[1]"
    eight_question_2 = "//table[@id='rows']/tbody[@class='answerSettingTextboxes']/tr[4]/td[1]/div/div[1]"
    eight_question_3 = "//table[@id='rows']/tbody[@class='answerSettingTextboxes']/tr[5]/td[1]/div/div[1]"
    eight_question_4 = "//table[@id='rows']/tbody[@class='answerSettingTextboxes']/tr[6]/td[1]/div/div[1]"
    eight_question_5 = "//table[@id='rows']/tbody[@class='answerSettingTextboxes']/tr[7]/td[1]/div/div[1]"

    # Ten Question
    ten_question_pattern = "//ul[@class='add-q-menu-left']//a[text()='Comment Box']"

    def save_button(self):
        self.wait_for_element(locator=self._question_save_button, locator_type="xpath", timeout=5, pollFrequency=1)
        time.sleep(5)
        self.element_click(self._question_save_button, locator_type="xpath")

    def next_question(self):
        self.wait_for_element(locator=self._add_new_question, locator_type="xpath", timeout=5, pollFrequency=1)
        time.sleep(5)
        self.element_click(self._add_new_question, locator_type="xpath")

    def enter_question_type(self):
        self.element_click(self._enter_question_type)

    # def commonall_question_pattern(self):
    #     self.element_click(self.third_nine_question_pattern)
    #
    # def commonall_question_select_pattern(self):
    #     self.wait_for_element(self.third_nine_question_select_pattern, locator_type="xpath", timeout=5, pollFrequency=1)
    #     self.element_click(self.third_nine_question_select_pattern)

    def first_question(self, first_question_enter=""):
        time.sleep(5)
        self.send_keys(first_question_enter, self._enter_question)
        AskQuestion.enter_question_type(self)
        self.element_click(self.first_question_pattern, locator_type="xpath")
        AskQuestion.save_button(self)
        AskQuestion.next_question(self)

    def second_question(self, second_question_enter=""):
        time.sleep(5)
        self.send_keys(second_question_enter, self._enter_question)
        AskQuestion.enter_question_type(self)
        self.element_click(self.second_question_pattern, locator_type="xpath")
        self.element_click(self.second_question_select_pattern, locator_type="xpath")
        AskQuestion.save_button(self)
        AskQuestion.next_question(self)

    def four_question(self, four_question_enter=""):
        time.sleep(5)
        self.send_keys(four_question_enter, self._enter_question)
        AskQuestion.enter_question_type(self)
        self.element_click(self.four_question_pattern, locator_type="xpath")
        AskQuestion.save_button(self)
        AskQuestion.next_question(self)

    def third_question(self, third_question_enter=""):
        time.sleep(5)
        self.send_keys(third_question_enter, self._enter_question)
        AskQuestion.enter_question_type(self)
        self.element_click(self.third_nine_question_pattern, locator_type="xpath")
        self.wait_for_element(self.third_nine_question_select_pattern, locator_type="xpath", timeout=5, pollFrequency=1)
        self.element_click(self.third_nine_question_select_pattern, locator_type="xpath")
        self.element_click(self.third_question_select_specific, locator_type="xpath")
        AskQuestion.save_button(self)
        AskQuestion.next_question(self)

    def five_question(self, five_question=""):
        time.sleep(5)
        self.send_keys(five_question, self._enter_question)
        AskQuestion.enter_question_type(self)
        self.element_click(self.five_question_pattern, locator_type="xpath")
        self.wait_for_element(self.third_nine_question_select_pattern, locator_type="xpath", timeout=5, pollFrequency=1)
        self.element_click(self.third_nine_question_select_pattern, locator_type="xpath")
        self.element_click(self.five_nine_question_select_specific, locator_type="xpath")
        AskQuestion.save_button(self)
        AskQuestion.next_question(self)

    def nine_question(self, nine_question_enter=""):
        time.sleep(5)
        self.send_keys(nine_question_enter, self._enter_question)
        AskQuestion.enter_question_type(self)
        self.element_click(self.third_nine_question_pattern, locator_type="xpath")
        self.wait_for_element(self.third_nine_question_select_pattern, locator_type="xpath", timeout=5, pollFrequency=1)
        self.element_click(self.third_nine_question_select_pattern, locator_type="xpath")
        self.element_click(self.five_nine_question_select_specific, locator_type="xpath")
        AskQuestion.save_button(self)
        AskQuestion.next_question(self)

    def ten_question(self, ten_question_enter=""):
        time.sleep(5)
        self.send_keys(ten_question_enter, self._enter_question)
        AskQuestion.enter_question_type(self)
        self.element_click(self.ten_question_pattern, locator_type="xpath")
        AskQuestion.save_button(self)
        AskQuestion.next_question(self)

    def six_question(self, six_question_enter=""):
        time.sleep(5)
        self.send_keys(six_question_enter, self._enter_question)
        AskQuestion.enter_question_type(self)
        self.element_click(self.six_question_pattern, locator_type="xpath")
        AskQuestion.six_question_special_type(self)
        AskQuestion.save_button(self)
        AskQuestion.next_question(self)

    def six_question_special_type(self):
        self.send_keys(six_1, self.six_question_1, locator_type="xpath")
        self.send_keys(six_2, self.six_question_2, locator_type="xpath")
        self.send_keys(six_3, self.six_question_3, locator_type="xpath")
        self.send_keys(six_4, self.six_question_4, locator_type="xpath")
        self.send_keys(six_5, self.six_question_5, locator_type="xpath")

    def seven_question(self, seven_question_enter=""):
        time.sleep(5)
        self.send_keys(seven_question_enter, self._enter_question)
        AskQuestion.enter_question_type(self)
        self.wait_for_element(locator=self.seven_question_pattern, locator_type="xpath", pollFrequency=1)
        self.element_click(self.seven_question_pattern, locator_type="xpath")
        AskQuestion.seven_question_special_type(self)
        AskQuestion.save_button(self)
        AskQuestion.next_question(self)

    def seven_question_special_type(self):
        self.send_keys(seven_1, self.seven_question_1, locator_type="xpath")
        self.send_keys(seven_2, self.seven_question_2, locator_type="xpath")
        self.send_keys(seven_3, self.seven_question_3, locator_type="xpath")
        self.send_keys(seven_4, self.seven_question_4, locator_type="xpath")
        self.send_keys(seven_5, self.seven_question_5, locator_type="xpath")
        self.send_keys(seven_6, self.seven_question_6, locator_type="xpath")
        self.send_keys(seven_7, self.seven_question_7, locator_type="xpath")

    def eight_question(self, eight_question_enter=""):
        time.sleep(5)
        self.send_keys(eight_question_enter, self._enter_question)
        AskQuestion.enter_question_type(self)
        self.wait_for_element(locator=self.eight_question_pattern, locator_type="xpath", pollFrequency=1)
        self.element_click(self.eight_question_pattern, locator_type="xpath")
        AskQuestion.eight_question_special_type(self)
        AskQuestion.save_button(self)
        AskQuestion.next_question(self)

    def eight_question_special_type(self):
        self.send_keys(six_1, self.eight_question_1, locator_type="xpath")
        self.send_keys(six_2, self.eight_question_2, locator_type="xpath")
        self.send_keys(six_3, self.eight_question_3, locator_type="xpath")
        self.send_keys(six_4, self.eight_question_4, locator_type="xpath")
        self.send_keys(six_5, self.eight_question_5, locator_type="xpath")

    def verify_question(self):
        self.wait_for_element(locator=self._survey_body, timeout=5, pollFrequency=1)
        result = self.is_element_present(locator=self._survey_body)
        return result

