#coding: utf-8
from unittesting.controller_test_cases import ControllerTestCases

class loginControllerTest(ControllerTestCases):

    def test_loginPage(self):
        self.assertCode('/admin/login', 200)
