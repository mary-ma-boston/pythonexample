# -*- coding: utf-8 -*- 
from selenium import webdriver
from time import sleep
import os

dr = webdriver.Chrome()
file_path = 'file:///' + os.path.abspath('GetAttribute.html')
dr.get(file_path)
link = dr.find_element_by_id('tooltip')
sleep(10)
# get the attribute of tooltip
#print(link.get_attribute('data-original-title'))
print(link.get_attribute('tooltip'))
# get the text 
print(link.text)
dr.quit()