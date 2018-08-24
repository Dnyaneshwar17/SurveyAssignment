from selenium.webdriver.common.by import By
from  base.Driver_method import SeleniumDriver
from base.Basepage import BasePage

class Login(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    login = "LOG IN"
    login_username = "username"
    login_password = "password"
    usernamet= "mauli123"
    passwordt = "m@uli123"
    _login_success="userAcctTab_MainMenu"
    _login_failed="//div[@id='sign-in']//li[contains(text(),'The username or password you entered is incorrect')]"
    _login_submit = "//form[@id='sign_in_form']//button[@type='submit']"

    def login_click(self):
        self.element_click(self.login, locator_type="link")

    def email(self,email):
        self.send_keys(email, self.login_username)

    def password(self,password):
        self.send_keys(password, self.login_password)

    def submit(self):
        self.element_click(self._login_submit, locator_type="xpath")

    def login_successful(self):
        self.wait_for_element(locator=self._login_success, timeout=5,pollFrequency=1)
        result = self.is_element_present(locator=self._login_success)
        return result

    def login_failed(self):
        result = self.is_element_present(locator=self._login_fail,locator_type="xpath")
        return result



    def startlogin(self, email="", password=" "):
        Login.login_click(self)
        Login.email(self, email)
        Login.password(self, password)
        Login.submit(self)







