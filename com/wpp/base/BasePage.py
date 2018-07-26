# coding=utf-8
_author_='wpp'

#super class
class BasePage(object):
    def __init__(self,driver):
        self.driver = driver