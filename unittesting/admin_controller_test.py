# coding: utf-8
from unittesting.controller_test_cases import ControllerTestCases

class adminControllerTest(ControllerTestCases):

    def test_adminPage(self):
        self.assertCode('/admin', 302)
