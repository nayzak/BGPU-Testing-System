# coding: utf-8
from unittesting.runTests import ControllerTestCases

class studentTest(ControllerTestCases):

    def setUp(self):
        print("SetUP")

    def tearDown(self):
        print("tearDown")

    def testPost(self):
        print("test_1")

    def testDelete(self):
        print("test_2")
