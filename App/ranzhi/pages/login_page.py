# Auto:达实泽林
# Creat Time:2021/12/22 17:43
# Creat Function:登录模块
# Edit Auto:
# Edit Time:
# Edit Function:

from base.box import BoxDriver, BaseDriver, YamlHelper, PathHelper


class LoginPage(BaseDriver):
    yaml_path = 'ranzhi\\pages\\page.yaml'
    path_helper = PathHelper()
    # 实例化YamlHelper，得到LoginPage的外层数据
    login_data = YamlHelper().get_yaml_data(path_helper.get_path(yaml_path))['LoginPage']

    def login_page(self, name, pwd):
        driver = self.base_driver
        # 打开项目页面
        url = 'http://localhost:8081/ranzhi/www'
        driver.get(url)
        # 隐式等待
        driver.implicitly_wait(20)
        # 最大化浏览器窗口
        driver.maximize_window()
        # 输入用户名，密码，点击登录
        driver.send_keys(self.login_data['LOGIN_NAME'], name)
        driver.send_keys(self.login_data['LOGIN_PWD'], pwd)
        driver.click(self.login_data['LOGIN_BUTTON'])


# 代码运行入口
if __name__ == '__main__':
    driver = BoxDriver('Chrome')
    LoginPage(driver).login_page('admin', '123456')
