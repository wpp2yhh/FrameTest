# coding=utf-8
_author_='wpp'

from selenium import webdriver
import unittest
import time
from ..base.LoginPage import LoginPage
from .TestCaseInfo import TestCaseInfo
from ..util.TestReport import TestReport

class Test_Login(unittest.TestCase):

    #Setup
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(30)
        self.base_url = "http://hr.huaqin.com/"
        #test case information
        self.testcaseinfo = TestCaseInfo(id="3",name="Login to HR manager system using 102003646",owner="wpp")
        self.testResult = TestReport()

    def test_Login(self):
        try:
            self.testcaseinfo.starttime = str(time.asctime())
            # Step1:open base site
            self.driver.get(self.base_url)
            # Step2:open login page
            login_page = LoginPage(self.driver)
            # Step3:Enter username
            login_page.set_usernameByName("102003646","UserID");
            # Step4:Enter password
            login_page.set_passwordByName("123456","Passwrd")
            # Step5:Click loginBtn
            login_page.click_loginByXPath("/html/body/div[2]/form/div/div[5]/a[1]/div/input")
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


