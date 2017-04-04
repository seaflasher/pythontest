# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException,\
NoAlertPresentException
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import xlrd
import xlwt

import unittest, time

class QuestCls(object):
    def __init__(self, quesno=0, questcont='', anwser=''):
        self._quesno = quesno
        self._questcont = questcont
        self._anwser = anwser
    
    def quesno(self):
        return self._quesno
    
    def questcont(self):
        return self._questcont
    
    def anwser(self):
        return self._anwser
   
data = xlrd.open_workbook('checklist.xlsx')
table = data.sheets()[0] # 打开第一张表
nrows = table.nrows

# 問題番号
questNoLst = []
# 問題内容リスト
questContentLst = []
# 問題答えリスト
questAnswerLst = []

for i in range(nrows):
    if i == 0:
        continue
    strRow = table.cell_value(i,1)
    print strRow
    rowslist = strRow.split(",")
    questNoLst.append(rowslist[0])
    questContentLst.append(rowslist[2])
    questAnswerLst.append(rowslist[3])

    #questinst = QuestCls(quesno=rowslist[0], questcont=rowslist[2], anwser=rowslist[3])
    #questlist.insert(i,questinst)
    print strRow[1:4]

#dicQuest(i).append(strRow[3:30])

def searchAnswer(lstQuestNo, lstAnswer, questNo):
    print "answerlst length", len(lstQuestNo)
    print "questNo", questNo
    
    for i in range(len(lstQuestNo)):

        if (str(lstQuestNo[i]).replace("'", "") == str(questNo)):
            return  str(lstAnswer[i]).replace("'", "")
    return ""

print "excel read over"

driver = webdriver.Ie("C:\Program Files (x86)\Internet Explorer\IEDriverServer.exe")
driver.implicitly_wait(30)
base_url = "http://dlcds3021:8080/s2chk/"
driver.verificationErrors = []
driver.accept_next_alert = True
driver.get(base_url)

#login in
driver.find_element_by_id("login_user_userId").send_keys("terry.xiaohui.wang")
driver.find_element_by_id("login_user_userPWD").send_keys("1111")
driver.find_element_by_id("login_0").click()


linklist = driver.find_elements_by_link_text("週次意識強化")
if len(linklist) <= 0:
    print "list error"
    exit

#
linklist[0].click()

# POP UP WINDOWS ACCEPT
a1 = driver.switch_to_alert().accept()
driver.implicitly_wait(1) # 隐性等待，最长等30秒

Select(driver.find_element_by_id("checklist_checkDate")).select_by_index(1)

# 週次チェック自動回答開始
for i in range(0,25):

    print "i=" + str(i)
    question_00=driver.find_element_by_id("checklist_questions_"+ str(i) + "__questionId").get_attribute('value')
    print "question00" + question_00
    driver.implicitly_wait(2)
    answer_tmp = searchAnswer(questNoLst, questAnswerLst, question_00)
    print "answer_tmp=" + answer_tmp
    if str(answer_tmp).strip() == '0':
        driver.find_element_by_id("checklist_questions_" + str(i) + "__standardAnswer0").click()
        driver.implicitly_wait(1)
    else:
        driver.find_element_by_id("checklist_questions_" + str(i) + "__standardAnswer1").click()       
        driver.implicitly_wait(1)

# 答えているかどうかチェック
for i in range(0,25):
    print "i=" + str(i)
    radiobtnYes = driver.find_element_by_id("checklist_questions_" + str(i) + "__standardAnswer0")
    radiobtnNo = driver.find_element_by_id("checklist_questions_" + str(i) + "__standardAnswer1")
    if radiobtnYes.is_selected() or radiobtnNo.is_selected():
        continue
    else:
        question_00=driver.find_element_by_id("checklist_questions_"+ str(i) + "__questionId").get_attribute('value')
        answer_tmp = searchAnswer(questNoLst, questAnswerLst, question_00)
    print "answer_tmp=" + answer_tmp
    
    if str(answer_tmp).strip() == '0':
        radiobtnYes.click()
        driver.implicitly_wait(1)
    else:
        radiobtnNo.click()       
        driver.implicitly_wait(1)

# テストが終わってSubmitする
driver.find_element_by_id("checklist_0").click()
