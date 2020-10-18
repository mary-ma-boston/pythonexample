# -*- coding: utf-8 -*- 
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep
import os

dr = webdriver.Chrome()
file_path = 'file:///' + os.path.abspath('ButtonDropdown.html')
dr.get(file_path)
sleep(1)
# locate the second button
buttons = dr.find_element_by_class_name('well').find_elements_by_class_name('btn')
for btn in buttons:
	if btn.text == 'second': print('find second button')
sleep(1)
dr.quit()