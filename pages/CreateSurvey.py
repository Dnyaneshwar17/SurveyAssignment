from selenium.webdriver.common.by import By
from utilities_config.Input import InputParameter
import time

class CreateSurvey(object):
      createtext = "CREATE SURVEY"
      first_survey_title = "surveyTitle"
      survey_send_key = "Goverment"
      #entry ="//*[@id='scratch']/span"
      entryscratch="scratch"

      survey_selection = "//div[@class='Select-placeholder']"
      survey_sel_final = "//div[@id='react-select-2--option-0']"
      survey_sel_create = "//button[@class='wds-button' and text()='CREATE SURVEY']"


      def createsurvey(self, driver):
          time.sleep(2)
          driver.find_element_by_link_text(CreateSurvey.createtext).click()
          #craetesurvey = driver.find_element(By.XPATH,'//*[@id="hd"]/div/div/a[2]')
          return True


      def survename(self, driver):
          surveyname = driver.find_element(By.ID, CreateSurvey.first_survey_title)
          surveyname.send_keys(CreateSurvey.survey_send_key)
          return True


      def surveyselection(self, driver):
          driver.find_element(By.XPATH, CreateSurvey.survey_selection).click()
          driver.find_element(By.XPATH, CreateSurvey.survey_sel_final).click()
          driver.find_element(By.XPATH, CreateSurvey.survey_sel_create).click()

        #finalcreate = driver.find_element_by_xpath("//button[@class='wds-button']").click()
        #finalcreate=driver.find_element_by_link_text("CREATE SURVEY").click()
        # surveyselection=driver.find_element(By.ID,"react-select-2--option-3").click()

          return True

      def entry(self, driver):
          driver.find_element(By.ID, CreateSurvey.entryscratch).click()
          return True

   # def removepopup(self,driver):
   #     alertobj=driver.switch_to.alert
   #     alertobj.accept()
   #     alertobj.dismiss()
   #
   #     remoove = driver.find_element(By.XPATH,"a[@class='wds-button wds-button--sm wds-button--ghost'][contains(text(),'REMOVE')]")
   #     remoove.click()
   #     return True