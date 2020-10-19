# -*- coding: utf-8 -*- 
from selenium import webdriver
from time import sleep
import os
if 'HTTP_PROXY'in os.environ: del os.environ['HTTP_PROXY']
dr = webdriver.Chrome()
file_path = 'file:///' + os.path.abspath('GetStatus.html')
dr.get(file_path)
text_field = dr.find_element_by_name('user')
print(text_field.is_enabled())
# Directly use is_enabled() to determine the button will return true
# Because button use css to disabled,not really disable
# You need to determin whether it is diaable in the class 
print(dr.find_element_by_class_name('btn').is_enabled())
# Hide text_field
# Whether it is display
dr.execute_script('$(arguments[0]).hide()', text_field)
print(text_field.is_displayed())
# Use click() to select radio
radio = dr.find_element_by_name('radio')
radio.click()
print(radio.is_selected())
# Whether the element exists
try:
	dr.find_element_by_id('none')
except: 
	print('element does not exist')
sleep(10)
dr.quit()
