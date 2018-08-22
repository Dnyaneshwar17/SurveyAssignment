from pages.StartSurvey import StartSurvey
from utilities_config.Browser import BrowserConfig
from pages.Login import Login
from pages.CreateSurvey import CreateSurvey
from pages.AskQuestion import AskQuestion
import time

class Start(object):


 def StartApp(self):
      driver=BrowserConfig.chrome(self)

      if Login.loginelement(self,driver):
         Login.username(self,driver)
         Login.password(self,driver)
         Login.submit(self,driver)

         if CreateSurvey.createsurvey(self,driver):
            CreateSurvey.entry(self,driver)
            CreateSurvey.survename(self,driver)
            CreateSurvey.surveyselection(self,driver)
            time.sleep(2)

            if StartSurvey.surveyedit(self,driver):
               time.sleep(2)
               StartSurvey.surveytitle(self,driver)
               time.sleep(5)

            else:
                print("Survey Edit is Failed")
         else:
          print("Create Survey Failed")

      else:
        print("Lgin Failed Please Check the detalis")



      if  AskQuestion.firstque(self,driver):
          AskQuestion.newquestion(self, driver)

          if AskQuestion.secondque(self,driver):
             AskQuestion.newquestion(self, driver)

             if AskQuestion.thirdque(self,driver):
                AskQuestion.newquestion(self, driver)

                if AskQuestion.fourque(self,driver):
                   AskQuestion.newquestion(self,driver)

                   if AskQuestion.fiveque(self,driver):
                      AskQuestion.newquestion(self,driver)

                      AskQuestion.sixque(self, driver)
                      AskQuestion.newquestion(self, driver)

                      AskQuestion.sevenque(self, driver)
                      AskQuestion.newquestion(self, driver)

                      AskQuestion.eightque(self, driver)
                      AskQuestion.newquestion(self, driver)



                      if AskQuestion.nineque(self,driver):
                         AskQuestion.newquestion(self,driver)

                         if AskQuestion.tenque(self,driver):
                            AskQuestion.newquestion(self,driver)
                         else:
                            print("Ten Failed")
                      else:
                          print("Nine Que Failed")


                   else:
                       print("Five Question Failed")

                else:
                    print("Four Question Failed")

             else:
                 print("Third Question Failed")

          else:
            print("Second Question Failed")
      else:
        print("First Question Failed")


Start().StartApp()
