# -*- coding: utf-8 -*-
from selenium import webdriver
import json
from jsonpath import jsonpath
driver = webdriver.PhantomJS()
test5 = open("ceshi5",'a')
for i in range(1,105):
    test5.write("第"+str(i)+"页"+'\n')
    driver.get('https://comment.dmzj.com/v1/4/latest/43400?callback=comment_list_s&page_index=' + str(i))
    html = driver.page_source
    html2 = html[103:-22]
    json2 = json.loads(html2)
    centents = jsonpath(json2,"$..content")
    nicknames = jsonpath(json2,"$..nickname")
    for nickname,centent in zip(nicknames,centents):
        test5.write(nickname+' '+centent+'\n')