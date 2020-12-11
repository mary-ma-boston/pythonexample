from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import os

class TestAmazonCart:
    myChrome = ''

    def setup_method(self):
        self.myChrome = webdriver.Chrome("chromedriver.exe")
        self.myChrome.implicitly_wait(5)
        self.myChrome.get("https://www.amazon.com/")

    def test_empty_cart(self):
        cart = self.myChrome.find_elements_by_id('nav-cart')
        cart.click()
        actual = self.myChrome.find_elements_by_xpath("//h1[@class='a-spacing-mini a-spacing-top-base']")
        actual_text = actual.text()
        expected_text = 'Your Amazon Cart is empty'
        
        assert expected_text == actual_text, f'Error Expect text：{expected_text}，but Actual text：{actual_text}'
   
    