from selenium import webdriver
from utilities_config.Input import InputParameter
import os


class BrowserConfig(object):
 def chrome(self):
     driverLocation = "D:\\Automation\\chromedriver"
     os.environ["webdriver.chrome.driver"] = driverLocation
     driver = webdriver.Chrome(driverLocation)
     driver.get(InputParameter.url)
     driver.maximize_window()
     return driver


 def firebox(self):
      driver = webdriver.Firefox()
      driver.get(InputParameter.url)
      driver.maximize_window()
      return driver


 def ie(self):
     driverLocation = "D:\\Automation\\IEDriverServer.exe"
     os.environ["webdriver.ie.driver"] = driverLocation
     driver = webdriver.Ie(driverLocation)
     driver.get(InputParameter.url)
     driver.maximize_window()
     return driver
