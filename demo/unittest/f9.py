# -*- coding:utf-8 -*-
#人生苦短，我用Python
#Author:Z

import unittest
# from selenium import webdriver
from demo.init import *
class BaiduLink(Init):
    def test_baidu_news(self):
        self.driver.find_element_by_link_text('新闻').click()

    def test_002(self):
        self.driver.find_element_by_link_text('地图').click()

    @staticmethod
    def suite():
        suite = unittest.TestSuite(unittest.makeSuite(BaiduLink))
        return suite

if __name__ == '__main__':
    unittest.TextTestRunner(verbosity=2).run(BaiduLink.suite())