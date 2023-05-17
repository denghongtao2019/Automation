#Auto:达实泽林
#Creat Time:2021/12/27 9:33
#Creat Function:运行测试用例，生成测试报告，发送报告邮件
#Edit Auto:
#Edit Time:
#Edit Function:

import unittest

from base.box import EmailHelper
from base.html_test_runner import HTMLTestRunner


class TestRunner:
    def test_runner(self):
        #创建测试套件的对象
        test_suite = unittest.TestSuite()
        #组织用例，定义规则，start_dir是用例所在目录，pattern是具体的匹配规则
        test_suite.addTests(unittest.TestLoader().discover(start_dir='cases',pattern='*_test.py'))
        #创建报告文件
        report_path = 'results\\reports\\ranzhi.html'
        report_file = open(report_path,mode='wb')
        #执行用例
        run_test = HTMLTestRunner(stream=report_file,title='然之协同自动化测试报告',description='测试用例详情')
        run_test.run(test_suite)
        #发送测试报告邮件
        # email_title = '然之协同自动化测试报告'
        # email_receiver = 's2338397498@163.com;XT128100701@163.com;yxc15701661649@163.com'
        # EmailHelper().email_send_163(report_path,email_title,email_receiver)

if __name__ == '__main__':
    TestRunner().test_runner()

