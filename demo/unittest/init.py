# -*- coding:utf-8 -*-
#人生苦短，我用Python
#Author:Z

import unittest
from selenium import webdriver

class Init(unittest.TestCase):
    def setUp(self):
        self.driver=webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.implicitly_wait(30)
        self.driver.get('http://www.baidu.com')

    def tearDown(self):
        self.driver.quit()