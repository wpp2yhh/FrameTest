# coding=utf-8
_autor_='wpp'

import unittest
from selenium import webdriver
from .TestCaseInfo import TestCaseInfo
from ..util.TestReport import TestReport
import time
from ..base.LoginPage import LoginPage
from selenium.webdriver.common.by import By


class Test_Login_OA(unittest.TestCase):

    #Setup
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(30)
        self.base_url = "http://oa.huaqin.com"
        # test case information
        self.testcaseinfo = TestCaseInfo(id="1", name="Login to OA manager system using 102003646", owner="wpp")
        self.testResult = TestReport()

    def test_Login(self):
        try:
            self.testcaseinfo.starttime = str(time.asctime())
            # Step1:open base site
            self.driver.get(self.base_url)
            # Step2:open login page
            login_page = LoginPage(self.driver)
            # Step3:Enter username
            login_page.set_usernameByName("102003646", "tbLoginName");
            # Step4:Enter password
            login_page.set_passwordByName("Asdqwe123456", "tbPassword")
            # Step5:Click loginBtn
            login_page.click_loginById("login-botton")
            time.sleep(30)
            self.testcaseinfo.result = "Pass"
        except Exception as err:
            print("wpp,----Test_Login-test_Login-err")
            self.testcaseinfo.errorinfo = str(err)
        finally:
            print("wpp,----Test_Login-test_Login-finally")
            self.testcaseinfo.endtime = str(time.asctime())

    #TeadDowm
    def tearDown(self):
        self.driver.close()
        print("wpp,----Test_Login-tearDown")
        #write test result
        #self.testResult.WriteResult(self.testcaseinfo)
        self.testResult.WriteHtmlResult(self.testcaseinfo)

if __name__ == '__main__':
        unittest.main()