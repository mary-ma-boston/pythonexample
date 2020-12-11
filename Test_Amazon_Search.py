from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import os

myChrome = webdriver.Chrome("chromedriver.exe")
myChrome.implicitly_wait(5)
myChrome.get("https://www.amazon.com/")

search = myChrome.find_element_by_id("twotabsearchtextbox")
search.send_keys('dress', Keys.ENTER)

expected_text= '''"dress"'''
actual = myChrome.find_element_by_xpath("//span[@class = 'a-color-state a-text-bold']")
actual_text = actual.text
#actual_text = actual_text.strip("\"")

assert expected_text == actual_text, f'Error Expect text：{expected_text}，but Actual text：{actual_text}'