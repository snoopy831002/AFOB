import requests
from bs4 import BeautifulSoup
from selenium import webdriver

requestURL = 'https://ifoodie.tw/ranking/weekly/%E5%8F%B0%E5%8D%97/' 
driver = webdriver.PhantomJS(executable_path=r'/Users/zhonghaoli/Downloads/phantomjs-2.1.1-macosx/bin/phantomjs')  # PhantomJS
driver.get(requestURL)
pageSource = driver.page_source 
soup = BeautifulSoup(pageSource, 'html.parser')
result = soup.findAll("h4",{"class","title"})
for i in result: 
     print(i.a['href'])