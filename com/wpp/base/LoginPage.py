# coding=utf-8
_author_='wpp'

from selenium.webdriver.common.by import By
from .BasePage import BasePage

class LoginPage(BasePage):

    #page element identifier
    usename = (By.NAME,'UserID')
    password = (By.NAME,'Passwrd')
    longinBtn = (By.XPATH,'/html/body/div[2]/form/div/div[5]/a[1]/div/input')

    #Get username textbox and imput username
    def set_username(self,username):
        name = self.driver.find_element(*LoginPage.usename)
        name.send_keys(username)

    #Get password textbox and input passowrd
    def set_password(self,password):
        pwd = self.driver.find_element(*LoginPage.password)
        pwd.send_keys(password)

    #Get "login" button and then click
    def click_login(self):
        loginbtn = self.driver.find_element(*LoginPage.longinBtn)
        loginbtn.click()