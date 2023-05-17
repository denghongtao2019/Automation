#Auto:达实泽林
#Creat Time:2021/12/21 19:25
#Creat Function:创建文档库、创建文档、编辑文档
#Edit Auto:
#Edit Time:
#Edit Function:

import action
from actions import Actions
from selenium import webdriver
#导入os模块
import os
# 导入time
import time
# 导入处理下拉框的类Select
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.webdriver import WebDriver
from selenium.webdriver.support.ui import Select
# 导入mysql
import pymysql
#导入键盘操作类
from selenium.webdriver.common.keys import Keys

# 实例化浏览器的对象
from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Chrome()
#隐式等待,全局，写在代码的最前面，作用于所有代码
driver.implicitly_wait(10)
# 定义一个变量url接收项目地址
url = 'http://localhost:8081/ranzhi/www'
# 浏览器打开请求地址
driver.get(url)
# 当前页面窗口最大化
driver.maximize_window()
# 输入账号
driver.find_element(By.ID,'account').send_keys('admin')
# 输入密码
driver.find_element(By.ID,'password').send_keys('123456')
# 点击登录按钮
driver.find_element(By.ID,'submit').click()

#点击文档按钮
driver.find_element(By.XPATH,'//div[@id="apps-menu"]/ul[1]/li[5]/button/img').click()
#切换frame（注意点 1）
driver.switch_to.frame('iframe-4')
#点击创建文档库按钮
driver.find_element(By.ID,'createButton').click()
#输入文档库名称
driver.find_element(By.ID,'name').send_keys('文档库01')
#选择授权用户(注意点 2，要定位到input,并点击“授权用户”)
driver.find_element(By.XPATH,'//div[@id="users_chosen"]/ul/li/input').send_keys('admin',Keys.ENTER)
time.sleep(1)
driver.find_element(By.XPATH,'//tr[@id="userTR"]/th').click()
time.sleep(1)
#选择授权分组
driver.find_element(By.ID,'groups1').click()
driver.find_element(By.ID,'groups2').click()
driver.find_element(By.ID,'groups3').click()
driver.find_element(By.ID,'groups4').click()
driver.find_element(By.ID,'groups5').click()
#点击保存按钮
driver.find_element(By.ID,'submit').click()
time.sleep(3)
#维护分类
#点击维护分类按钮
driver.find_element(By.LINK_TEXT,'维护分类').click()
#输入类目（注意点 3）
eles_classify = driver.find_elements(By.ID,'children[]')
eles_classify[0].send_keys('测试部')
eles_classify[1].send_keys('研发部')
eles_classify[2].send_keys('财务部')
eles_classify[3].send_keys('行政部')
eles_classify[4].send_keys('业务部')
#点击保存
driver.find_element(By.ID,'submit').click()

#返回自定义文档库页面（注意点 4）
#点击首页
driver.find_element(By.LINK_TEXT,'首页').click()
#点击新建的文档库
driver.find_element(By.LINK_TEXT,'文档库01').click()

#点击创建文档
driver.find_element(By.CSS_SELECTOR,'a.btn:nth-child(3)').click()
#选择所属分类（注意点 5）
# 1.定位下拉框
ele_dept = driver.find_element(By.ID,'module')
# 2.引入Select类对下拉框操作
select_dept = Select(ele_dept)
# 3.对下拉框内容进行选择
select_dept.select_by_visible_text('/测试部')
#选择授权用户
driver.find_element(By.XPATH,'//div[@id="users_chosen"]/ul/li/input').send_keys('admin',Keys.ENTER)
time.sleep(1)
driver.find_element(By.XPATH,'//tr[@id="userTR"]/th').click()
time.sleep(1)
#选择授权分组
driver.find_element(By.ID,'groups1').click()
driver.find_element(By.ID,'groups2').click()
driver.find_element(By.ID,'groups3').click()
driver.find_element(By.ID,'groups4').click()
driver.find_element(By.ID,'groups5').click()
#输入文档标题
doc_title = '文档标题001'
driver.find_element(By.ID,'title').send_keys(doc_title)
#切换iframe
driver.switch_to.frame('ueditor_0')
#输入文档正文
driver.find_element(By.XPATH,'/html/body').send_keys('文档正文')
#切换iframe(注意点 6)，退出到iframe最外层：driver.switch_to.default_content()
# 退出到上一层：driver.switch_to.parent_frame()
driver.switch_to.default_content()
driver.switch_to.frame('iframe-4')
#输入关键字
driver.find_element(By.ID,'keywords').send_keys('正文')
#输入文档摘要
driver.find_element(By.ID,'digest').send_keys('正文很好')
#滚动到上传附件的位置
# 定位目标元素
ele = driver.find_element(By.XPATH,'//table[@id="fileBox1"]/tbody/tr/td[1]/div/input')
# 下拉滚动条的js脚本,固定写法，不需要修改
js = 'arguments[0].scrollIntoView()'
# 运行js脚本，下拉滚动条到上面的定位元素
driver.execute_script(js, ele)
#上传附件（注意点 7）
#方式1
#当上传功能标签为input，tpye属性值为file时，可以把上传功能当作是往一个输入框内写入内容来处理，写入的内容是附件的路径
# driver.find_element_by_xpath('//table[@id="fileBox1"]/tbody/tr/td[1]/div/input').send_keys(r'D:\PythonCode\ranzhi\附件01.txt')
#方式2
#如果上传功能标签不是input，那么上传附件就要借助其他的工具来辅助操作，autoit V3
#步骤：1.打开AutoIt Window Info（x64）界面
#2.聚焦到窗口的文件路径输入框，获取Title、ClassnameNIN（即controlID）
#3.聚焦到窗口的确定按钮，获取ClassnameNIN（即控件ID）
#4.编写操作脚本另存后缀名为au3的文件
#ControlFocus("title","窗口文本","controlID") 设置输入焦点到指定窗口的某个控件上
#WinWait("title","窗口文本",超时时间) 暂停脚本的执行直至指定窗口存在（出现）为止
#ControlSetText("title","窗口文本","controlID","文件路径") 修改指定控件的文本
#Sleep(延迟) 使脚本暂停指定时间，单位是毫秒
#ControlClick("title","窗口文本","控件ID") 向指定控件发送鼠标点击命令
#5.用Compile Script to.exe（x64） 将au3文件转换成python可执行的exe文件
#6.调用os模块函数执行
#点击上传按钮；停顿；调用os模块函数选择附件

ele_fj = driver.find_element(By.XPATH,'//table[@id="fileBox1"]/tbody/tr/td[1]/div/input')
ActionChains(driver).move_to_element(ele_fj).click().perform()
time.sleep(3)
os.system(r'D:\PythonCode\class2021.10.20\ranzhi\脚本.exe')
#点击保存按钮
driver.find_element(By.ID,'submit').click()
time.sleep(3)
#点击文档编号，倒序排列
driver.find_element(By.LINK_TEXT,'文档编号').click()
#添加断言，判断文档是否添加成功
assert driver.find_element(By.LINK_TEXT,'%s'%doc_title).text == doc_title,'添加文档失败'
print('添加文档成功')

#编辑文档标题
#点击文档编号，倒序排列
driver.find_element(By.LINK_TEXT,'文档编号').click()
#获取所有的编辑按钮
ele_edit = driver.find_elements(By.XPATH,'//table[@id="docList"]/tbody/tr/td[6]/a[1]')
#点击新添加文档的编辑按钮
ele_edit[0].click()
#修改文档标题
doc_title_edit = '文档标题0011'
driver.find_element(By.ID,'title').clear()
driver.find_element(By.ID,'title').send_keys(doc_title_edit)
#点击保存按钮
driver.find_element(By.ID,'submit').click()
time.sleep(3)
#点击返回按钮
driver.find_element(By.LINK_TEXT,'返回').click()

#点击文档编号，倒序排列
driver.find_element(By.LINK_TEXT,'文档编号').click()
#添加断言，判断文档是否修改成功
assert driver.find_element(By.LINK_TEXT,'%s'%doc_title_edit).text == doc_title_edit,'修改文档失败'
print('修改文档成功')

#关闭所有浏览器
driver.quit()


