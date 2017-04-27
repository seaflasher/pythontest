# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException,\
NoAlertPresentException
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

import unittest, time

driver = webdriver.Ie("C:\Program Files (x86)\Internet Explorer\IEDriverServer.exe")
driver.implicitly_wait(30)
base_url = "myte.accenture.com"
driver.verificationErrors = []
driver.accept_next_alert = True
driver.get(base_url)

#login in
#driver.find_element_by_id("userNameInput").send_keys("terry.xiaohui.wang")
#driver.find_element_by_id("passwordInput").send_keys("Syjc^6789")
#driver.find_element_by_id("submitButton").click()

'''
locator = (By.LINK_TEXT, 'CSDN')  
try:  
    WebDriverWait(driver, 20, 0.5).until(EC.presence_of_element_located(locator))  
    print driver.find_element_by_link_text('CSDN').get_attribute('href')  
finally:  
    driver.close()
'''
driver.implicitly_wait(10) # 隐性等待，最长等30秒 

linklist = driver.find_elements_by_link_text("Reports")
if len(linklist) <= 0:
    print "list error"
    exit
#
linklist[0].click()
driver.implicitly_wait(10) # 隐性等待，最长等30秒 

selectLst = driver.find_elements_by_tag_name("SELECT")
for i in range(len(selectLst)):
    print "hehe"
print "get select list"

Select(driver.find_element_by_id("ctl00_MainContentPlaceHolder_ddl_Reports")).select_by_value('ForecastedTimeDetails')
driver.implicitly_wait(10) # 隐性等待，最长等30秒 


Select(driver.find_element_by_id("ctl00_MainContentPlaceHolder_ddl_EndDates_dropdownTimePeriod")).select_by_value('2017/03/31')
driver.implicitly_wait(10) # 隐性等待，最长等30秒 

selectLst = driver.find_elements_by_tag_name("SELECT")

for i in range(len(selectLst)):
    print selectLst[i].name
    #selectLst[i].select_by_index(2)


#dateselect = Select(driver.find_element_by_id("ctl00_MainContentPlaceHolder_ddl_StartDates_*")).options()
#Select(driver.find_element_by_id("ctl00_MainContentPlaceHolder_ddl_StartDates_dropdownTimePeriod")).select_by_value('2017/03/31')

driver.implicitly_wait(30) # 隐性等待，最长等30秒 



