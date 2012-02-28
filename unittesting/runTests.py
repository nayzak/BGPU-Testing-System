# coding: utf-8
import unittest

class ControllerTestCases(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        print("init db")


    @classmethod
    def tearDownClass(cls):
        print("drop db")

if __name__ == '__main__':
    unittest.main()
