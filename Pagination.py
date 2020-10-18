# -*- coding: utf-8 -*- 
from selenium import webdriver
from time import sleep
import os
import time

dr = webdriver.Chrome()
file_path = 'file:///' + os.path.abspath('pagination.html')
dr.get(file_path)
# get the number of all pages
# use -2 is for removing the previous page and the next page
total_pages = len(dr.find_element_by_class_name('pagination').find_elements_by_tag_name('li')) - 2
print("total page is %s"%(total_pages))
# get the url of current page and current page
current_page = dr.find_element_by_class_name('pagination').find_element_by_class_name('active')
print("current page is %s"%(current_page.text))
time.sleep(10)
dr.quit()

