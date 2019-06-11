# -*- coding:utf-8 -*-
#人生苦短，我用Python
#Author:Z

import unittest

class F1(unittest.TestCase):

    def setUp(self):
        print('开始著被工作完毕')

    def tearDown(self):
        print('以处理')

    def test_01(self):
        print('test')

    def test_02(self):
        print('test')

    def test_03(self):
        pass

if __name__ == '__main__':
    unittest.main(verbosity=2)
