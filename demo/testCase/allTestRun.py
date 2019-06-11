# -*- coding:utf-8 -*-
#人生苦短，我用Python
#Author:Z

'''
批量执行测试用例代码
'''
import  unittest
import  os
import  HtmlTestRunner
import  time

def allTest():
    #获取文件目录，以及test文件
    suite = unittest.TestLoader().discover(
        start_dir=os.path.dirname(__file__),
        pattern='test_*.py',
        top_level_dir=None)
    return suite

#运行函数
def getNowTime():
	return time.strftime("%Y-%m-%d %H_%M_%S",time.localtime(time.time()))

def run():
	fp=os.path.join(os.path.dirname(__file__),'report',getNowTime()+'testReport.html')
	HtmlTestRunner.HTMLTestRunner(
		stream=open(fp,'wb'),
		report_title='自动化测试报告',
		).run(allTest())

if __name__ == '__main__':
	run()


