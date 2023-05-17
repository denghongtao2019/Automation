#Auto:达实泽林
#Creat Time:2021/12/22 17:52
#Creat Function:用户测试用例模块
#Edit Auto:
#Edit Time:
#Edit Function:

import unittest
import time

from parameterized import parameterized
from base.box import BoxDriver, ExcelHelper, AssertHelper, LogHelper, PathHelper
from pages.login_page import LoginPage
from pages.user_page import UserPage


class UserTest(unittest.TestCase):
    driver = BoxDriver('Chrome')
    excel_path = 'ranzhi\\cases\\add_user_data.xlsx'
    path_helper = PathHelper()
    excel_file = path_helper.get_path(excel_path)
    sheet_name = 'user_page'
    excel_helper = ExcelHelper()
    add_user_data = excel_helper.get_excel_data(excel_file, sheet_name)
    log_path = 'ranzhi\\results\\logs\\add_user.log'
    log_helper = LogHelper(path_helper.get_path(log_path))


    @classmethod
    def setUpClass(self):
        LoginPage(self.driver).login_page('admin', '123456')
        self.user_page = UserPage(self.driver)
        self.user_page.before_add_user()

    @classmethod
    def tearDownClass(self):
        # 退出浏览器
        self.driver.quit()

    @parameterized.expand(add_user_data)
    def test_user_success(self,row,name,real_name,dept,role,pwd1,pwd2,email,tips_except,type,result):
        try:
            if type == 'success':
                self.user_page.add_user(name,real_name,dept,role,pwd1,pwd2,email)
                #获取页面和数据表中的最新添加的用户名
                name_text = self.user_page.get_name_text()
                name_result = self.user_page.get_name_result(name)
                # 断言
                AssertHelper().assert_equal(name_text,name)
                AssertHelper().assert_equal(name_result,name)
                #把测试通过的结果写入excel表
                self.excel_helper.write_excel_data(
                    self.excel_file, self.sheet_name,int(row)+1,11,'通过')
                self.log_helper.info('results\\logs\\test_user_success_%s_断言通过，'
                                     '测试通过的结果已写入excel'%row)
                # 点击左侧添加成员按钮，进入添加成员页面
                self.user_page.click_adduser_button()
        except:
            #获取用例未通过的截图
            self.driver.get_screenshot_as_file(
                'results\\screenshots\\test_user_success_%s_%s.png'%(
                    row,time.strftime('%Y-%m-%d_%H-%M-%S')))
            self.log_helper.info('test_user_success_%s_断言未通过，截图已保存' % row)
            # 把测试未通过的结果写入excel表
            self.excel_helper.write_excel_data(
                self.excel_file, self.sheet_name, int(row) + 1, 11, '未通过')
            self.log_helper.info('results\\logs\\test_user_success_%s_断言未通过，'
                                 '测试未通过的结果已写入excel' % row)
    @parameterized.expand(add_user_data)
    def test_user_fail(self,row,name,real_name,dept,role,pwd1,pwd2,email,tips_except,type,result):
        try:
            if type == 'fail':
                self.user_page.add_user(name,real_name,dept,role,pwd1,pwd2,email)
                #获取用户添加失败的页面提示
                tips = self.user_page.get_add_user_fail_tips()
                # 断言
                AssertHelper().assert_equal(tips,tips_except)
                # 把测试通过的结果写入excel表
                self.excel_helper.write_excel_data(
                    self.excel_file, self.sheet_name, int(row) + 1, 11, '通过')
                self.log_helper.info('test_user_fail_%s_断言通过，测试通过的结果已写入excel'%row)

        except:
            # 获取用例未通过的截图
            self.driver.get_screenshot_as_file(
                'results\\screenshots\\test_user_fail%s_%s.png' % (row, time.strftime('%Y-%m-%d_%H-%M-%S')))
            self.log_helper.info('results\\logs\\test_user_fail_%s_断言未通过，截图已保存' % row)
            # 把测试未通过的结果写入excel表
            self.excel_helper.write_excel_data(
                self.excel_file, self.sheet_name, int(row) + 1, 11, '未通过')
            self.log_helper.info('results\\logs\\test_user_fail_%s_断言未通过，'
                                 '测试未通过的结果已写入excel' % row)

if __name__ == '__main__':
    unittest.main()
