#Auto:达实泽林
#Creat Time:2021/12/24 16:36
#Creat Function:
#Edit Auto:
#Edit Time:
#Edit Function:

from selenium import webdriver
import time

driver = webdriver.Chrome()
driver.get('https://www.baidu.com')
time.sleep(2)

driver.get_screenshot_as_file('234.png')
driver.get_screenshot_as_file('345.jpg')
driver.get_screenshot_as_file('456.gif')
driver.quit()