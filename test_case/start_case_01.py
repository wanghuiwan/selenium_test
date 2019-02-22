# -*- coding: utf-8 -*-

import unittest
from ddt import ddt,data,unpack
from function.function_01 import *
# 用例
datedd = [{"names":"qad_martin01",'password':'123456'},{"names":"qad_martin01",'password':'123456'}]
@ddt
class Case_aaaa(unittest.TestCase):
    """哇塞好玩"""

    @classmethod
    def setUpClass(cls):
        # logins("zongdai0001", 'zongdai0001')
        pass


    @data(*datedd[:])
    # @unpack
    def testasdf(self,a):
        print(a)
        namess = a['names']
        password = a['password']
        logins(namess,password)
        quit()

    def tearDownClass(cls):
        pass



if __name__ == "__main__":
    unittest.main()