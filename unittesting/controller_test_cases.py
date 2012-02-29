# coding: utf-8
'''
 run tests: python -m unittest discover -s root_directory -p '*_test.py'

'''
import unittest
from webunit.webunittest import WebTestCase

class ControllerTestCases(WebTestCase):

    def setUp(self):
        self.setServer('localhost', '8000')

