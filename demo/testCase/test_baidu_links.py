# -*- coding:utf-8 -*-
#人生苦短，我用Python
#Author:Z

from selenium import webdriver
import unittest

class BaiduLink(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get('http://www.baidu.com')

    def tearDown(self):
        self.driver.quit()

    def test_baidu_news(self):
        '''首页,点击新闻是否可以正常跳转'''
        self.driver.find_element_by_link_text('新闻').click()
        self.assertEqual(self.driver.current_url,'http://news.baidu.com/')

    def test_baidu_map(self):
        '''首页,点击地图是否可以正常跳转'''
        self.driver.find_element_by_link_text('地图').click()
        self.assertEqual(self.driver.current_url,'https://map.baidu.com/@12954547,4835865,13z')

if __name__ == '__main__':
    unittest.main(verbosity=2)