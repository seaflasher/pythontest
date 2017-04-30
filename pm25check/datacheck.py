# coding:utf-8
import threading
import urllib
import re,sys
import time
import hashlib
import os


def getPageContent():

    while True:
        
        temp='http://data.eastmoney.com/zjlx/'
        url = urllib.urlopen(temp)
        text = url.read()
        myItems=re.findall('<div.*?class="flash-data-cont flash-data-cont-line">(.*?)</div>',text,re.S)
        
        for item in myItems:
            content=item.strip()
            print 'content' + content 
        
        items=[]


getPageContent()