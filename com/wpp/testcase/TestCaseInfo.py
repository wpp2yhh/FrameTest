# coding=utf-8
_author_='wpp'

import unittest

class TestCaseInfo(object):
    """description of class"""

    def __init__(self,id="",name="",owner="",result="Failed",starttime="",endtime="",errorinfo=""):
        self.id = id
        self.name = name
        self.owner = owner
        self.result = result
        self.starttime = starttime
        self.endtime = endtime
        self.errorinfo = errorinfo

if __name__ == '__main__':
    unittest.main()