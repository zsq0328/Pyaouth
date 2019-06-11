# -*- coding:utf-8 -*-
#人生苦短，我用Python
#Author:Z

'''
类方法
'''

import unittest
from selenium import webdriver

class F2(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver=webdriver.Chrome()
        cls.driver.maximize_window()
        cls.driver.implicitly_wait(30)
        cls.driver.get('http://www.baidu.com')

    @classmethod
    def tearDownclass(cls):
        cls.driver.quit()

    def test_baidu_news(self):
        self.driver.find_element_by_link_text('新闻').click()
        self.driver.back()

    def test_baidu_map(self):
        self.driver.find_element_by_link_text('地图').click()
        self.driver.back()

if __name__ == '__main__':
    unittest.main(verbosity=2)