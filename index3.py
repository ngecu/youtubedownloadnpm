# Generated by Selenium IDE
import time
import json
from selenium import webdriver
from selenium.webdriver.common.by import By
import os


from selenium.webdriver.chrome.options import Options

options = Options()
options.add_argument('--headless')
options.add_argument('--disable-gpu')  # Last I checked this was necessary.
driver = webdriver.Chrome(chrome_options=options)

driver = webdriver.Chrome()

driver.get("https://www.xvideos.com/?k=reality+show")
elements = driver.find_elements_by_class_name('thumb')


myLinks=driver.find_elements_by_xpath("//div[@class='thumb']/a")
for link in myLinks:
    how = link.get_attribute("href")
    code = "you-get {}".format(how)
    print(how)
    os.system(code)

driver.close()

