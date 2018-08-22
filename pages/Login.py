from selenium.webdriver.common.by import By
from utilities_config.Input import InputParameter

class Login(object):

	login = "LOG IN"
	login_username ="username"
	login_password = "password"
	usernamet = "mauli123"
	passwordt = "m@uli123"
	login_submit = "//form[@id='sign_in_form']//button[@type='submit']"

	def loginelement(self,driver):
		driver.find_element_by_link_text(Login.login).click()
		return True

	def username(self, driver):
		user = driver.find_element(By.ID,Login.login_username)
		user.send_keys(Login.usernamet)
		return True


	def password(self, driver):
		password = driver.find_element(By.ID,Login.login_password)
		password.send_keys(Login.passwordt)
		return True

	def submit(self,driver):
		driver.find_element(By.XPATH,Login.login_submit).click()
		return True

	def startlogin(self, driver):
		Login.loginelement(self, driver)
		Login.username(self, driver)
		Login.password(self, driver)
		Login.submit(self, driver)
		return True









