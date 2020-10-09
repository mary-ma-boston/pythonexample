import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


myChrome = webdriver.Chrome("chromedriver.exe")
myChrome.get("https://www.glassdoor.com/Job/boston-qa-jobs-SRCH_IL.0,6_IC1154532_KE7,9.htm")



allJobTitle = ""
first = True
# get the job title 
ulElement = myChrome.find_element_by_xpath('''/html/body/div[3]/div/div/div[1]/div/div[2]/section/article/div[1]/ul''')
allLiElements = ulElement.find_elements_by_xpath(".//li")
for liEle in allLiElements:
    liEle.click()
    time.sleep(5)
    try:
        closeEle = myChrome.find_element_by_xpath("//span[@class='SVGInline modal_closeIcon']")
        if closeEle != None:
            closeEle.click()
            time.sleep(5)
    except:
        pass

    try:
        jobDescElemet = myChrome.find_element_by_id("JobDescriptionContainer")
        allJobTitle += liEle.text + "\n---------------------------------\n"
        allJobTitle += jobDescElemet.text + "\n****************************\n"
    except:
        pass

fileOutput = open("JobTitle.txt", "w", encoding='utf-8')
fileOutput.write(allJobTitle)
fileOutput.close()

print(allJobTitle)
myChrome.close()
time.sleep(10)

