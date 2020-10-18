# -*- coding: utf-8 -*-

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
myChrome = webdriver.Chrome("chromedriver.exe")
myChrome.get("http://www.python.org")
time.sleep(3)
# click
myChrome.find_element_by_xpath("/html/body/div/header/div/nav/ul/li[2]").click()
time.sleep(3)

# send_keys
elem = myChrome.find_element_by_name("q")
elem.send_keys("verson")
elem.send_keys(Keys.RETURN)


# clear
# elem.clear()
time.sleep(10)
myChrome.quit()
