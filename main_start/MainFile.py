from pages.StartSurvey import StartSurvey
from utilities_config.Browser import BrowserConfig
from pages.Login import Login
from pages.CreateSurvey import CreateSurvey



class Start(object):

      def StartApp(self):

          driver = BrowserConfig.chrome(self)

          if Login.startlogin(self, driver):
              CreateSurvey.startcreatesurvey(self, driver)
              print("Create Survey Done..!!!")
              if StartSurvey.startsurvey(self, driver):
                  print("Done All Question")
              else:
                  print("Survey Question ")
          else:
              print("Login Failed Failed")


Start().StartApp()
