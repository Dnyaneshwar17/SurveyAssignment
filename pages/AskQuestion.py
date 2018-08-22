from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
import time

class AskQuestion(object):

       question_typing = "//div[@id ='editTitle']"
       question_ans_patt = "//a[@id='changeQType' and @class='sm-input']"
       question_save_butt = "//div[@id='editQuestion']/section[@class='t1']//a[text()='SAVE']"

       # First Question:
       first_que_sendkey = "Enter your email..?"
       first_que_ans_patt = "//ul[@class='add-q-menu-left']//a[text()='Single Textbox']"

       # Second Question:
       second_que_sendkey = "From when you are using Survey Monkey.?"
       second_que_ans_patt = "//ul[@class='add-q-menu-right']//a[text()='Date / Time']"
       second_que_ans_patt2 = "//table[@id='rows']/tfoot[@class='answerTableFooter']//label[.='Time Info']"

       # Third Question:
       third_que_sendkey = "How often do you use SurveyMonkey?"
       third_que_ans_patt = "//ul[@class='add-q-menu-left']//a[text()='Multiple Choice']"
       third_que_sel = "//div[@id='editQuestion']//select[@id='answerBankCategorySelect']"
       third_que_sel_specific = "Always - Never"

       # Four Question:
       four_que_sendkey = "How will rate the ease of survey creation?"
       four_que_ans_patt = "//ul[@class='add-q-menu-left']//a[text()='Star Rating']"

       # Five Question:
       five_que_sendkey = "Did you get meaningful data from survey analysis?"
       five_que_ans_patt = "//ul[@class='add-q-menu-right']//a[text()='Dropdown']"

       five_que_sel = "//div[@id='editQuestion']//select[@id='answerBankCategorySelect']"
       five_que_sel_specific = "Yes - No"

       # Six Question:

       six_que_sendkey = "Check the Features you like about SurveyMonkey?"
       six_que_ans_patt = "//ul[@class='add-q-menu-left']//a[text()='Checkboxes']"

       six_que_sel1 = "//table[@id='rows']/tbody[@class='answerSetting singleLine']/tr[4]/td[2]/div/div[1]"
       six_que_skey1 = "Question Bank"

       six_que_sel2 = "//table[@id='rows']/tbody[@class='answerSetting singleLine']/tr[5]/td[2]/div/div[1]"
       six_que_skey2 = "Themes"

       six_que_sel3 = "//table[@id='rows']/tbody[@class='answerSetting singleLine']/tr[6]/td[2]/div/div[1]"
       six_que_skey3 = "Graphical Result"

       six_que_sel4 = "//table[@id='rows']/tbody[@class='answerSetting singleLine']/tr[7]/td[2]/div/div[1]"
       six_que_skey4 = "Template Re-usability"

       six_que_sel5 = "//table[@id='rows']/tbody[@class='answerSetting singleLine']/tr[8]/td[2]/div/div[1]"
       six_que_skey5 = "Collectors"


       #seven Question:
       seven_que_sendkey="Rate our features. (Matrix Rating Scale)"
       seven_que_ans_patt="//ul[@class='add-q-menu-right']//a[text()='Matrix / Rating Scale']"

       seven_que_sel1="//table[@id='rows']/tbody[@class='answerSettingMatrix singleLine']/tr[3]/td[1]/div/div[1]"
       seven_que_skey1="Service"

       seven_que_sel2="//table[@id='rows']/tbody[@class='answerSettingMatrix singleLine']/tr[4]/td[1]/div/div[1]"
       seven_que_skey2="Support"

       seven_que_sel3="//table[@id='rows']/tbody[@class='answerSettingMatrix singleLine']/tr[5]/td[1]/div/div[1]"
       seven_que_skey3="Responsive"

       seven_que_sel4="//div[@id='columnsWrap']//table/tbody[@class='columnSetting singleLine']/tr[2]/td[1]/div/div[1]"
       seven_que_skey4="Very Good"

       seven_que_sel5="//div[@id='columnsWrap']//table/tbody[@class='columnSetting singleLine']/tr[3]/td[1]/div/div[1]"
       seven_que_skey5="Good"

       seven_que_sel6="//div[@id='columnsWrap']//table/tbody[@class='columnSetting singleLine']/tr[4]/td[1]/div/div[1]"
       seven_que_skey6="Average"

       seven_que_sel7="//div[@id='columnsWrap']//table/tbody[@class='columnSetting singleLine']/tr[5]/td[1]/div/div[1]"
       seven_que_skey7="Below Average"


       # Eight Question

       eight_que_sendkey = "List the features you like most."
       eight_que_ans_patt = "//ul[@class='add-q-menu-right']//a[text()='Multiple Textboxes']"

       eight_que_sel1 = "//table[@id='rows']/tbody[@class='answerSettingTextboxes']/tr[3]/td[1]/div/div[1]"
       eight_que_skey1 = "Question Bank"

       eight_que_sel2 = "//table[@id='rows']/tbody[@class='answerSettingTextboxes']/tr[4]/td[1]/div/div[1]"
       eight_que_skey2 = "Themes"

       eight_que_sel3 = "//table[@id='rows']/tbody[@class='answerSettingTextboxes']/tr[5]/td[1]/div/div[1]"
       eight_que_skey3 = "Graphical Result"

       eight_que_sel4 = "//table[@id='rows']/tbody[@class='answerSettingTextboxes']/tr[6]/td[1]/div/div[1]"
       eight_que_skey4 = "Template Re-usability"

       eight_que_sel5 = "//table[@id='rows']/tbody[@class='answerSettingTextboxes']/tr[7]/td[1]/div/div[1]"
       eight_que_skey5 = "Collectors"






       # Nine Question
       nine_que_sendkey = "Will recommend SurveyMonkey to your friends / Colleagues?"
       nine_que_ans_patt = "//ul[@class='add-q-menu-left']//a[text()='Multiple Choice']"
       # "//div[@id='editQuestion']//select[@id='answerBankCategorySelect']"

       # Ten Question
       ten_que_sendkey = "Comments / Feedback (Text-area)"
       ten_que_ans_patt = "//ul[@class='add-q-menu-left']//a[text()='Comment Box']"


       def firstque(self, driver):
           time.sleep(2)
           firstq = driver.find_element(By.XPATH,AskQuestion.question_typing)
           firstq.send_keys(AskQuestion.first_que_sendkey)
           time.sleep(2)
           driver.find_element(By.XPATH,AskQuestion.question_ans_patt).click()
           time.sleep(5)
           driver.find_element(By.XPATH,AskQuestion.first_que_ans_patt).click()
           time.sleep(5)
           driver.find_element(By.XPATH,AskQuestion.question_save_butt).click()
           time.sleep(5)
           return True



       def secondque(self,driver):
           secque=driver.find_element(By.XPATH,AskQuestion.question_typing)
           time.sleep(3)
           secque.send_keys(AskQuestion.second_que_sendkey)
           time.sleep(2)
           driver.find_element(By.XPATH, AskQuestion.question_ans_patt).click()
           time.sleep(3)
           driver.find_element(By.XPATH,AskQuestion.second_que_ans_patt).click()
           time.sleep(3)
           driver.find_element(By.XPATH,AskQuestion.second_que_ans_patt2).click()
           time.sleep(5)
           driver.find_element(By.XPATH,AskQuestion.question_save_butt).click()
           time.sleep(3)
           return True


       def thirdque(self,driver):
           thirdque=driver.find_element(By.XPATH,AskQuestion.question_typing)
           time.sleep(3)
           thirdque.send_keys(AskQuestion.third_que_sendkey)
           time.sleep(3)
           driver.find_element(By.XPATH, AskQuestion.question_ans_patt).click()
           time.sleep(3)
           driver.find_element(By.XPATH,AskQuestion.third_que_ans_patt).click()
           time.sleep(3)
           question_type=driver.find_element(By.XPATH,AskQuestion.third_que_sel)
           time.sleep(3)
           sel = Select(question_type)
           sel.select_by_visible_text(AskQuestion.third_que_sel_specific)
           time.sleep(2)
           driver.find_element(By.XPATH,AskQuestion.question_save_butt).click()
           time.sleep(3)
           return True



       def fourque(self,driver):
           fourque=driver.find_element(By.XPATH,AskQuestion.question_typing)
           time.sleep(3)
           fourque.send_keys(AskQuestion.four_que_sendkey)
           time.sleep(3)
           driver.find_element(By.XPATH,AskQuestion.question_ans_patt).click()
           time.sleep(3)
           driver.find_element(By.XPATH,AskQuestion.four_que_ans_patt).click()
           time.sleep(3)
           driver.find_element(By.XPATH,AskQuestion.question_save_butt).click()
           time.sleep(3)
           return True

       def fiveque(self,driver):
           fiveque=driver.find_element(By.XPATH,AskQuestion.question_typing)
           time.sleep(2)
           fiveque.send_keys(AskQuestion.five_que_sendkey)
           time.sleep(3)
           driver.find_element(By.XPATH,AskQuestion.question_ans_patt).click()
           time.sleep(3)
           driver.find_element(By.XPATH,AskQuestion.five_que_ans_patt).click()
           time.sleep(3)
           question_type=driver.find_element(By.XPATH,AskQuestion.five_que_sel)
           sel = Select(question_type)
           sel.select_by_visible_text(AskQuestion.five_que_sel_specific)
           driver.find_element(By.XPATH,AskQuestion.question_save_butt).click()
           time.sleep(3)
           return True

       def sixque(self,driver):
           sixque = driver.find_element(By.XPATH, AskQuestion.question_typing)
           time.sleep(3)
           sixque.send_keys(AskQuestion.six_que_sendkey)
           driver.find_element(By.XPATH, AskQuestion.question_ans_patt).click()
           driver.find_element(By.XPATH, AskQuestion.six_que_ans_patt).click()
           time.sleep(5)
           question_type = driver.find_element(By.XPATH, AskQuestion.six_que_sel1)
           question_type.send_keys(AskQuestion.six_que_skey1)
           time.sleep(3)
           question_type= driver.find_element(By.XPATH, AskQuestion.six_que_sel2)
           question_type.send_keys(AskQuestion.six_que_skey2)
           time.sleep(3)
           question_type = driver.find_element(By.XPATH, AskQuestion.six_que_sel3)
           question_type.send_keys(AskQuestion.six_que_skey3)

           question_type = driver.find_element(By.XPATH,AskQuestion.six_que_sel4)
           question_type.send_keys(AskQuestion.six_que_skey4)
           question_type = driver.find_element(By.XPATH,AskQuestion.six_que_sel5)
           question_type.send_keys(AskQuestion.six_que_skey5)
           driver.find_element(By.XPATH, AskQuestion.question_save_butt).click()
           time.sleep(3)
           return True



       def sevenque(self,driver):
           sevenque = driver.find_element(By.XPATH, AskQuestion.question_typing)
           time.sleep(3)
           sevenque.send_keys(AskQuestion.seven_que_sendkey)
           driver.find_element(By.XPATH,AskQuestion.question_ans_patt).click()
           driver.find_element(By.XPATH,AskQuestion.seven_que_ans_patt).click()
           time.sleep(3)
           question_type = driver.find_element(By.XPATH,AskQuestion.seven_que_sel1)
           question_type.send_keys(AskQuestion.seven_que_skey1)
           question_type = driver.find_element(By.XPATH,AskQuestion.seven_que_sel2)
           question_type.send_keys(AskQuestion.seven_que_skey2)
           question_type = driver.find_element(By.XPATH,AskQuestion.seven_que_sel3)
           question_type.send_keys(AskQuestion.seven_que_skey3)
           question_type = driver.find_element(By.XPATH,AskQuestion.seven_que_sel4 )
           question_type.send_keys(AskQuestion.seven_que_skey4)

           question_type = driver.find_element(By.XPATH,AskQuestion.seven_que_sel5)
           question_type.send_keys(AskQuestion.seven_que_skey5)

           question_type = driver.find_element(By.XPATH,AskQuestion.seven_que_sel6)
           question_type.send_keys(AskQuestion.seven_que_skey6)

           question_type = driver.find_element(By.XPATH,AskQuestion.seven_que_sel7)
           question_type.send_keys(AskQuestion.seven_que_skey7)

           driver.find_element(By.XPATH, AskQuestion.question_save_butt).click()
           time.sleep(3)
           return True

       def eightque(self, driver):
           eightque = driver.find_element(By.XPATH, AskQuestion.question_typing)
           time.sleep(2)
           eightque.send_keys(AskQuestion.eight_que_sendkey)
           time.sleep(2)
           driver.find_element(By.XPATH, AskQuestion.question_ans_patt).click()
           driver.find_element(By.XPATH, AskQuestion.eight_que_ans_patt).click()

           question_type = driver.find_element(By.XPATH,AskQuestion.eight_que_sel1)
           question_type.send_keys(AskQuestion.eight_que_skey1)

           question_type = driver.find_element(By.XPATH,AskQuestion.eight_que_sel2)
           question_type.send_keys(AskQuestion.eight_que_skey2)

           question_type = driver.find_element(By.XPATH,AskQuestion.eight_que_sel3)
           question_type.send_keys(AskQuestion.eight_que_skey3)

           question_type = driver.find_element(By.XPATH,AskQuestion.eight_que_sel4)
           question_type.send_keys(AskQuestion.eight_que_skey4)

           question_type = driver.find_element(By.XPATH, AskQuestion.eight_que_sel5)
           question_type.send_keys(AskQuestion.eight_que_skey5)
           driver.find_element(By.XPATH, AskQuestion.question_save_butt).click()
           time.sleep(3)
           return True

       def nineque(self,driver):
           nineque = driver.find_element(By.XPATH, AskQuestion.question_typing)
           time.sleep(2)
           nineque.send_keys(AskQuestion.nine_que_sendkey)
           time.sleep(3)
           driver.find_element(By.XPATH, AskQuestion.question_ans_patt).click()
           time.sleep(3)
           driver.find_element(By.XPATH,AskQuestion.nine_que_ans_patt).click()
           time.sleep(3)
           question_type= driver.find_element(By.XPATH,AskQuestion.five_que_sel)
           time.sleep(2)
           sel= Select(question_type)
           sel.select_by_visible_text(AskQuestion.five_que_sel_specific)
           time.sleep(2)
           driver.find_element(By.XPATH,AskQuestion.question_save_butt).click()
           time.sleep(3)
           return True


       def tenque(self,driver):
           tenque=driver.find_element(By.XPATH, AskQuestion.question_typing)
           time.sleep(3)
           tenque.send_keys(AskQuestion.ten_que_sendkey)
           time.sleep(3)
           driver.find_element(By.XPATH, AskQuestion.question_ans_patt).click()
           time.sleep(3)
           driver.find_element(By.XPATH,AskQuestion.ten_que_ans_patt).click()
           time.sleep(3)
           driver.find_element(By.XPATH, AskQuestion.question_save_butt).click()
           time.sleep(3)
           return True


       def newquestion(self,driver):
           time.sleep(1)
           driver.find_element(By.XPATH,"//a[.='NEW QUESTION']").click()
           time.sleep(2)
           return  True

       def startquestion(self, driver):
           time.sleep(2)
           AskQuestion.firstque(self, driver)
           AskQuestion.newquestion(self, driver)
           time.sleep(3)


           AskQuestion.secondque(self,driver)
           AskQuestion.newquestion(self, driver)


           AskQuestion.thirdque(self,driver)
           AskQuestion.newquestion(self, driver)


           AskQuestion.fourque(self,driver)
           AskQuestion.newquestion(self,driver)


           AskQuestion.fiveque(self,driver)
           AskQuestion.newquestion(self,driver)

           AskQuestion.sixque(self, driver)
           AskQuestion.newquestion(self, driver)

           AskQuestion.sevenque(self, driver)
           AskQuestion.newquestion(self, driver)

           AskQuestion.eightque(self, driver)
           AskQuestion.newquestion(self, driver)



           AskQuestion.nineque(self,driver)
           AskQuestion.newquestion(self,driver)

           AskQuestion.tenque(self,driver)
           return True




