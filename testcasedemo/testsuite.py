import unittest
from testcasedemo.test_Login import TestLoginDemo

tc1 = unittest.TestLoader().loadTestsFromTestCase(TestLoginDemo)

smokeTest = unittest.TestSuite([tc1])
unittest.TextTestRunner(verbosity=2).run(smokeTest)