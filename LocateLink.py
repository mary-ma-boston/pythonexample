# -*- coding: utf-8 -*- 
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep
import os
if 'HTTP_PROXY'in os.environ: del os.environ['HTTP_PROXY']

dr = webdriver.Chrome()
file_path = 'file:///' + os.path.abspath('navs.html')

dr.get(file_path)

sleep(1)

# method1：Hierarchical locate，first locate ul and then link
dr.find_element_by_class_name('nav').find_element_by_link_text('About').click()
sleep(1)

# method2: Direct locate link
dr.find_element_by_link_text('Home').click()
sleep(1)

dr.quit()