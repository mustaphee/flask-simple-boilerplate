import unittest

testSuite = unittest.TestLoader().discover('./tests')
unittest.TextTestRunner(verbosity=3).run(testSuite)