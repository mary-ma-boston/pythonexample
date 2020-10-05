from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
myChrome = webdriver.Chrome("chromedriver.exe")

myChrome.get("http://www.python.org")
elem = myChrome.find_element_by_name("q")
elem.clear()
elem.send_keys("pyconasdfasfsadfasdfasdf")
elem.send_keys(Keys.RETURN)
time.sleep(10)
