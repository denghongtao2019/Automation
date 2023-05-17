#Auto:达实泽林
#Creat Time:2021/12/21 17:17
#Creat Function:添加区块、编辑区块
#Edit Auto:
#Edit Time:
#Edit Function:

import time
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

#实例化浏览器对象，使用变量driver来接收
driver = webdriver.Chrome()
#打开项目页面
url = 'http://localhost:8081/ranzhi/www'
driver.get(url)
#最大化浏览器窗口
driver.maximize_window()
#输入用户名，密码，点击登录
driver.find_element(By.ID,'account').send_keys('admin')
driver.find_element(By.ID,'password').send_keys('123456')
driver.find_element(By.ID,'submit').click()
#休眠2秒
time.sleep(2)
#隐式等待
driver.implicitly_wait(20)
#点击项目按钮
driver.find_element(By.XPATH,'//*[@id="s-menu-3"]/button').click()
#切换框架
driver.switch_to.frame('iframe-3')
time.sleep(3)
#点击添加区块
driver.find_element(By.CLASS_NAME,'btn-primary').click()
time.sleep(2)
#选择任务列表
Select(driver.find_element(By.ID,'blocks')).select_by_visible_text('任务列表')
time.sleep(2)
#输入区块名称
driver.find_element(By.ID,'title').send_keys('区块001')
#外观宽度选择1/4
Select(driver.find_element(By.ID,'grid')).select_by_visible_text('1/4')
#点击颜色选择按钮
driver.find_element(By.CLASS_NAME,'dropdown-toggle').click()
#选择颜色为绿色
eles_color = driver.find_elements(By.XPATH,'//*[@id="ajaxForm"]/'
                                           'table/tbody/tr[2]/td/div/div/div/div/li/button')
#获取元素的data-id属性值，利用属性值选择
for ele in eles_color:
    if ele.get_attribute('data-id') == 'success':
        ele.click()
#点击类型选择框
driver.find_element(By.CLASS_NAME,'chosen-single').click()
#类型选择由我创建
driver.find_element(By.XPATH,'//*[@id="paramstype_chosen"]'
                             '/div/div/input').send_keys('由我创建',Keys.ENTER)
#数量输入20
driver.find_element(By.ID,'params[num]').clear()
driver.find_element(By.ID,'params[num]').send_keys('20')
#点击排序选择框
driver.find_element(By.ID,'paramsorderBy_chosen').click()
#排序选择优先级递增
driver.find_element(By.XPATH,'//*[@id="paramsorderBy_chosen"]'
                             '/div/div/input').send_keys('优先级递增',Keys.ENTER)
#点击任务状态选择框
driver.find_element(By.ID,'paramsstatus_chosen').click()
#任务状态选择已完成
driver.find_element(By.CSS_SELECTOR,'.default').send_keys('已完成',Keys.ENTER)
#点击保存按钮
driver.find_element(By.ID,'submit').click()
time.sleep(5)
#针对数据较多的情况，拖拉滚动条找到下面的新添加的元素
# 定位目标元素
ele_edit = driver.find_elements(By.CLASS_NAME,'btn-mini')[-1]
# 下拉滚动条的js脚本,固定写法，不需要修改
js = 'arguments[0].scrollIntoView();'
# 运行js脚本，下拉滚动条到上面的定位元素
driver.execute_script(js, ele_edit)


#点击区块最右侧下箭头
#用class方式定位
driver.find_elements(By.CLASS_NAME,'btn-mini')[-1].click()
#点击编辑按钮
driver.find_elements(By.CLASS_NAME,'edit-block')[-1].click()
time.sleep(2)
#编辑区块名称
name = '区块0011'
driver.find_element(By.ID,'title').clear()
driver.find_element(By.ID,'title').send_keys(name)
#点击保存按钮
driver.find_element(By.ID,'submit').click()
time.sleep(3)
#获取区块列表最新编辑的区块名称做断言
result_name = driver.find_elements(By.CLASS_NAME,'panel-success')[-1].get_attribute('data-name')
assert result_name == name,'编辑区块名称失败'
print('编辑区块名称成功')
#关闭所有浏览器
driver.quit()

