from selenium import webdriver
import time
import os

dr = webdriver.Chrome()
file_path =  'file:///' + os.path.abspath('BreadCrumb.html')
dr.get(file_path)

# get the parent
for link in dr.find_element_by_class_name('breadcrumb').find_elements_by_tag_name('a'):
	print(link.text)

# get the current
# Since there maybe a lot of elements are active
# So using hierarchical positioning is the best
print(dr.find_element_by_class_name('breadcrumb').find_element_by_class_name('active').text)

time.sleep(5)
dr.quit()