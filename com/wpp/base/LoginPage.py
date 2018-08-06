# coding=utf-8
_author_='wpp'

from selenium.webdriver.common.by import By
from .BasePage import BasePage

class LoginPage(BasePage):

    #Get username textbox and imput username
    def set_usernameByName(self,userName,namePara):
        name = self.driver.find_element(By.NAME,namePara)
        name.send_keys(userName)

    #Get password textbox and input passowrd
    def set_passwordByName(self,passWord,pwdPara):
        pwd = self.driver.find_element(By.NAME,pwdPara)
        pwd.send_keys(passWord)

    #Get "login" button and then click
    def click_loginByXPath(self,loginPara):
        loginbtn = self.driver.find_element(By.XPATH,loginPara)
        loginbtn.click()

    def click_loginById(self,loginPara):
        loginbtn = self.driver.find_element(By.ID,loginPara)
        loginbtn.click()