# coding=utf-8

import os
from selenium import webdriver

driver=webdriver.Firefox()

driver.get('http://www.baidu.com')
<<<<<<< HEAD
driver.find_element_by_tag_name('input').send_keys('wqw')
=======
driver.find_element_by_tag_name('input').send_keys('asas')
>>>>>>> feature1
driver.quit()