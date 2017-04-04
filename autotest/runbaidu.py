# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException,\
NoAlertPresentException
import unittest, time

class Baidu(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Ie("C:\Program Files (x86)\Internet Explorer\IEDriverServer.exe")
        self.driver.implicitly_wait(30)
        self.base_url = "http://www.baidu.com/?tn=98012088_4_dg&ch=3"
        self.verificationErrors = []
        self.accept_next_alert = True
        self.driver.get(self.base_url)

    def test_baidu_search(self):
        '''百度搜索'''
        driver = self.driver
        try:
            driver.find_element_by_id("kw").send_keys("selenium webdriver")
            driver.find_element_by_id("su").click()
        except:
            driver.get_screenshot_as_file('D:\\workspace\\python_prictise\\src\\error.png')
        time.sleep(2)

    def test_baidu_set(self):
        '''百度新闻'''
        driver = self.driver
        driver.find_element_by_name("tj_trnews").click()
        time.sleep(2)
        self.assertEqual(driver.title,u'百度新闻搜索——全球最大的中文新闻平台',"switch to baidu news faile!")

    def is_element_present(self, how, what):
        try: self.driver.find_element(by=how, value=what)
        except NoSuchElementException: return False
        return True

    def is_alert_present(self):
        try: self.driver.switch_to_alert()
        except NoAlertPresentException: return False
        return True

    def close_alert_and_get_its_text(self):
        try:
            alert = self.driver.switch_to_alert()
            alert_text = alert.text
            if self.accept_next_alert:
                alert.accept()
            else:
                alert.dismiss()
            return alert_text
        finally: self.accept_next_alert = True

    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)

unittest.main()

