import os
import flask
import unittest
import tempfile

class FlaskrTestCase(unittest.TestCase):

    class Test1(TestCase):
    def UserCredentials_right(self):
        self.assertTrue(True)

    def UserCredentials_false(self):
        self.assertTrue(False)

if __name__ == '__main__':
    unittest.main()
