# coding=utf-8
_author_='wpp'

import subprocess

class Runtests(object):
    """description of class"""
    def __init__(self):
        self.testcaselistfile = "../doc/testcase.txt"

    #use nosetests command to execute test case list
    def LoadAndRunTestCases(self):
        try:
            f = open(self.testcaselistfile,'r', encoding='utf-8')
            testfiles = []
            for test in f:
                if not test.startswith("#"):
                    testfiles.append(test)
            print(testfiles)
            for item in testfiles:
                print("nosetests "+str(item).replace("\\n",""))
                subprocess.call("nosetests "+str(item).replace("\\n",""),shell=True)
        finally:
            print('>>>>>>finally')
            if f:
                f.close()

if __name__ == "__main__":
    newrun = Runtests()
    newrun.LoadAndRunTestCases()