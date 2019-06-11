# -*- coding:utf-8 -*-
#人生苦短，我用Python
#Author:Z

import unittest
# from selenium import webdriver
from demo.init import *

class BaiduLink(Init):
    def test_BaiDu_news(self):
        self.assertEqual(self.driver.title,'百度一下，你就知道')



if __name__ == '__main__':
    unittest.main(verbosity=2)