#Auto:达实泽林
#Creat Time:2021/12/22 11:44
#Creat Function:文件的下载
#Edit Auto:
#Edit Time:
#Edit Function:

from selenium import webdriver
from selenium.webdriver.common.by import By

# driver = webdriver.Chrome()

# driver.get('https://cmder.net')
#默认路径下载
# driver.find_element(By.ID,'mini').click()

#自定义路径下载
#指定下载路径
download_dir = {'download.default_directory':'D:\\'}
#实例化浏览器设置项类
get_option = webdriver.ChromeOptions()
#添加扩展项，prefs参数固定
get_option.add_experimental_option('prefs',download_dir)
#启动浏览器，临时改变浏览器下载选项
driver = webdriver.Chrome(options=get_option)
driver.get('https://github.com/cmderdev/cmder/releases/download/v1.3.18/cmder_mini.zip')

