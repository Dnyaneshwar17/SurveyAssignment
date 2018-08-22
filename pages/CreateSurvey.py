from selenium.webdriver.common.by import By
import time

class CreateSurvey(object):
      createtext = "CREATE SURVEY"
      first_survey_title = "surveyTitle"
      survey_send_key = "Goverment"
      entryscratch="scratch"

      survey_selection = "//div[@class='Select-placeholder']"
      survey_sel_final = "//div[@id='react-select-2--option-0']"
      survey_sel_create = "//button[@class='wds-button' and text()='CREATE SURVEY']"


      def createsurvey(self, driver):
          time.sleep(2)
          driver.find_element_by_link_text(CreateSurvey.createtext).click()
          return True


      def survename(self, driver):
          surveyname = driver.find_element(By.ID, CreateSurvey.first_survey_title)
          surveyname.send_keys(CreateSurvey.survey_send_key)
          return True


      def surveyselection(self, driver):
          driver.find_element(By.XPATH, CreateSurvey.survey_selection).click()
          driver.find_element(By.XPATH, CreateSurvey.survey_sel_final).click()
          driver.find_element(By.XPATH, CreateSurvey.survey_sel_create).click()
          return True

      def entry(self, driver):
          driver.find_element(By.ID, CreateSurvey.entryscratch).click()
          return True

      def startcreatesurvey(self, driver):
          CreateSurvey.createsurvey(self, driver)
          time.sleep(2)
          CreateSurvey.entry(self, driver)
          time.sleep(2)
          CreateSurvey.survename(self, driver)
          time.sleep(2)
          CreateSurvey.surveyselection(self, driver)
          return True

