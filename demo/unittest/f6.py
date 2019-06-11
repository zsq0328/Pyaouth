# -*- coding:utf-8 -*-
#人生苦短，我用Python
#Author:Z

import unittest
from selenium import webdriver

class F6(unittest.TestCase):

    def test_user_001(self):
        pass

    def test_user_002(self):
        pass


if __name__ == '__main__':
    suit = unittest.TestSuite
    #按照测试类来执行
    suit.addTest(F6)
    unittest.TextTestRunner(verbosity=2).run(suit)