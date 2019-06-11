# -*- coding:utf-8 -*-
#人生苦短，我用Python
#Author:Z

import unittest
from selenium import webdriver
from demo.init import *

class BaiduLink(Init):
    def test_baidu_news(self):
        self.driver.find_element_by_id('kw').send_keys('webdriver')

if __name__ == '__main__':
    unittest.main(verbosity=2)
