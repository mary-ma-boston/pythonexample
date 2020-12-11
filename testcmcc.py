from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

myChrome = webdriver.Chrome("chromedriver.exe")
myChrome.get("https://www.middlesex.mass.edu/")
#elem = myChrome.find_element_by_id("text-1")
elem = myChrome.find_element_by_xpath("/html/body/header/nav/div/div[2]/div/div/div/div/ul/li[1]/a")
elem.click()
# elem.clear()
# elem.send_keys("pyconasdfasfsadfasdfasdf")
# elem.send_keys(Keys.RETURN)
time.sleep(10)
