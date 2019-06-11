# -*- coding:utf-8 -*-
#人生苦短，我用Python
#Author:Z

'''
加载整个测试类
'''

import unittest
from selenium import webdriver

class F8(unittest.TestCase):

    def setUp(self):
        self.driver=webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.implicitly_wait(30)
        self.driver.get('http://www.baidu.com')

    def tearDown(self):
        self.driver.quit()

    def test_baidu_news(self):
        self.driver.find_element_by_link_text('新闻').click()

    def test_002(self):
        self.driver.find_element_by_link_text('地图').click()

if __name__ == '__main__':
    suit = unittest.TestLoader().loadTestsFromTestCase(F8)
    unittest.TextTestRunner(verbosity=2).run(suit)