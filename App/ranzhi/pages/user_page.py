# Auto:达实泽林
# Creat Time:2021/12/21 14:58
# Creat Function:添加成员
# Edit Auto:
# Edit Time:
# Edit Function:
import time

# 实例化浏览器对象，使用变量driver来接收

from base.box import BoxDriver, DbHelper, BaseDriver, YamlHelper, PathHelper
from pages.login_page import LoginPage


class UserPage(BaseDriver):
    yaml_path = 'ranzhi\\pages\\page.yaml'
    path_helper = PathHelper()
    # 实例化YamlHelper，得到UserPage的外层数据
    user_data = YamlHelper().get_yaml_data(path_helper.get_path(yaml_path))['UserPage']

    def before_add_user(self):
        '''
        添加成员前的操作
        :return:
        '''
        driver = self.base_driver
        time.sleep(5)
        # 点击后台管理按钮
        driver.click(self.user_data['MANAGE_BUTTON'])
        # 切换frame
        driver.switch_to_frame(self.user_data['FRAME'])
        # 点击添加成员按钮
        driver.click(self.user_data['ADD_BUTTON'])

    def add_user(self, name, real_name, dept, role, pwd1, pwd2, email):
        '''
        添加成员
        '''
        driver = self.base_driver
        # 输入用户名，也是预期结果
        driver.send_keys(self.user_data['USERNAME'], name)
        # 输入真实姓名
        driver.send_keys(self.user_data['REALNAME'], real_name)
        # 选择性别
        driver.click(self.user_data['SEX'])
        # 选择部门
        driver.select_by_visible_text(self.user_data['DEPT'], dept)
        # 选择角色
        driver.select_by_visible_text(self.user_data['ROLE'], role)
        # 输入密码和确认密码
        driver.send_keys(self.user_data['PWD1'], pwd1)
        driver.send_keys(self.user_data['PWD2'], pwd2)
        # 输入邮箱
        driver.send_keys(self.user_data['EMAIL'], email)
        # 点击保存按钮
        driver.click(self.user_data['SAVE_BUTTON'])
        # 休眠2秒
        time.sleep(2)

    def get_name_text(self):
        # 从页面和数据库获取最新添加的用户名，做断言
        # 点击编号列，倒序排列
        driver = self.base_driver
        driver.click(self.user_data['SERIAL_NUM'])
        # 获取页面最新添加的用户名
        name_text = driver.get_elements_text(self.user_data['ACTVALUE'], 0)
        return name_text

    def get_name_result(self, name):
        # 建立数据库连接
        mysql_connect = DbHelper(host='localhost', port=3306, username='root', pwd='', db_name='ranzhi')
        # 获取数据库最新添加的用户名
        sql = 'select account from sys_user where account = "%s"' % name
        result = mysql_connect.get_db_data(sql)
        name_result = result[0][0]
        mysql_connect.close_db()
        return name_result

    def click_adduser_button(self):
        # 点击左侧添加成员按钮，进入添加成员页面
        driver = self.base_driver
        driver.click(self.user_data['ADD_BUTTON1'])

    def get_add_user_fail_tips(self):
        # 获取用户添加失败的页面提示
        return self.base_driver.get_element_text(self.user_data['USER_FAIL_TEXT'])


# 代码运行入口
if __name__ == '__main__':
    driver = BoxDriver('Chrome')
    LoginPage(driver).login_page('admin', '123456')
    user_page = UserPage(driver)
    user_page.before_add_user()
    user_page.add_user('xiaoming', '小明', '/测试部', '高层管理', '123456', '123456', 'xiaoming@126.com')
