
from selenium.webdriver.common.by import By
from  pages.AskQuestion import AskQuestion
from utilities_config.Input import InputParameter
import time

class StartSurvey(object):


        createtitle = "title-text"
        surveyTitle = "//div[@id='surveyTitle']"
        new_survey_title = "Central Goverment"
        survey_save_final = "//*[@id='surveyTitleForm']//a[text()='SAVE']"
        page_title = "//span[text() = 'PAGE TITLE']"
        page_title_start = "//div[@id='pageTitle']"
        new_page_title = "New Page Title"
        page_title_save = "//*[@id='pageTitleForm']//a[text()='SAVE']"



        def surveyedit(self,driver):
            time.sleep(2)
            driver.find_element(By.CLASS_NAME, StartSurvey.createtitle).click()
            surveyedit=driver.find_element(By.XPATH,StartSurvey.surveyTitle)
            time.sleep(2)
            surveyedit.clear()
            time.sleep(1)
            surveyedit.send_keys(StartSurvey.new_survey_title)
            driver.find_element(By.XPATH,StartSurvey.survey_save_final).click()
            time.sleep(2)
            return True

        def surveytitle(self,driver):
            driver.find_element(By.XPATH,StartSurvey.page_title).click()
            time.sleep(1)
            surveytitle= driver.find_element_by_xpath(StartSurvey.page_title_start)
            time.sleep(1)
            surveytitle.send_keys(StartSurvey.new_page_title)
            driver.find_element(By.XPATH,StartSurvey.page_title_save).click()
            return True


        def startsurvey(self, driver):
            StartSurvey.surveyedit(self, driver)
            time.sleep(2)
            StartSurvey.surveytitle(self, driver)
            AskQuestion.startquestion(self, driver)




