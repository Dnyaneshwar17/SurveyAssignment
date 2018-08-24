from base.Driver_method import SeleniumDriver



class BasePage(SeleniumDriver):

    def __init__(self,driver):
        """
        Inits BasePage class
        Returns:
        None
        """
        self.driver = driver