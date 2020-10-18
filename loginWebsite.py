import urllib.request
import time
from selenium import webdriver

myChrome = webdriver.Chrome("chromedriver.exe")
myChrome.get ("https://github.com/login")
myChrome.find_element_by_id("login_field").send_keys("814948490@qq.com")
myChrome.find_element_by_id ("password").send_keys("mayue088318")
myChrome.find_element_by_name("commit").click()
time.sleep(10)

