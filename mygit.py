# coding=utf-8

import os
from selenium import webdriver

driver=webdriver.Firefox()

driver.get('http://www.baidu.com')

driver.quit()