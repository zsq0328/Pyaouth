# -*- coding:utf-8 -*-
#人生苦短，我用Python
#Author:Z

import unittest
# from selenium import webdriver
from demo.init import *

'''
unittest.skip:装饰器，忽略
unittest.expectedFailure:装饰器,期望用例失败
'''

def add(a,b):
    return a-b

class BaiduLink(Init):
    @unittest.skip('忽略此功能')
    def test_baidu_news(self):
        self.driver.find_element_by_link_text('新闻').click()

    def test_002(self):
        self.driver.find_element_by_link_text('地图').click()

    @unittest.expectedFailure
    def test_003(self):
        self.assertEqual(add(2-1),1)

if __name__ == '__main__':
    unittest.main(verbosity=2)