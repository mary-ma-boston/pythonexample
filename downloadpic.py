import urllib.request

from selenium import webdriver

import time

myChrome = webdriver.Chrome("chromedriver.exe")
myChrome.get("https://www.redfin.com/")

# get the image source
img = myChrome.find_element_by_xpath("/html/body/div[1]/div[6]/div[5]/section/div/div[1]/img")
src = img.get_attribute('src')

# download the image
data = urllib.request.urlretrieve(src, "C:\\Users\\kaixu\\Desktop\\Wife Code\\house.png")

myChrome.close()
time.sleep(10)