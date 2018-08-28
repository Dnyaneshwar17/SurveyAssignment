import unittest
from testcasedemo.test_login import TestLoginDemo
from testcasedemo.test_create_survey import TestCreateSurvey

class Test_Suite(unittest.TestCase):

    def test_main_class(self):

        self.suite = unittest.TestSuite()
        tc1 = unittest.TestLoader().loadTestsFromTestCase(TestLoginDemo)
        tc2 = unittest.TestLoader().loadTestsFromTestCase(TestCreateSurvey)

        self.suite.addTests([tc1, tc2])
        runner = unittest.TextTestRunner()
        runner.run(self.suite)