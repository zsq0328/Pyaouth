# -*- coding:utf-8 -*-
#人生苦短，我用Python
#Author:Z

'''
按照测试类执行
'''

import unittest
from selenium import webdriver

class F7(unittest.TestCase):

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_001(self):
        pass

    def test_002(self):
        pass

if __name__ == '__main__':
    suit = unittest.TestSuite(unittest.makeSuite(F7))
    unittest.TextTestRunner(verbosity=2).run(suit)