'''
  pttstupidCrawer.py
  @about-Parse data from weekly ranking from ifoodie according to city 
  Created by 中皓 李 on 2016/10/23.
  Copyright © 2016 中皓 李. All rights reserved.
'''
import requests 
from bs4 import BeautifulSoup #@note-(install via pip3)
from selenium import webdriver #@note-parse ajax call back from website(install via pip3)

#soup = BeautifulSoup('<script>a</script>baba<script>b</script>','html.parser')
#[s.extract() for s in soup('script')]
#print(soup)


requestURL = 'https://www.ptt.cc/bbs/StupidClown/M.1477234511.A.4AB.html' 
driver = webdriver.PhantomJS(executable_path=r'/Users/zhonghaoli/Downloads/phantomjs-2.1.1-macosx/bin/phantomjs') # PhantomJS
driver.get(requestURL)
pageSource = driver.page_source 
soup = BeautifulSoup(pageSource, 'html.parser')
result =soup.findAll("div",{"class","bbs-screen bbs-content"},{"id","main-content"})
[s.extract() for s in soup('span')]
[s.extract() for s in soup("div",{"class","push"})]
[s.extract() for s in soup("div",{"class","richcontent"})]
[s.extract() for s in soup("div",{"class","article-metaline"})]
[s.extract() for s in soup("div",{"class","article-metaline-right"})]
[s.extract() for s in soup('a')]
for i in result:
	print(i.text)
#[s.extract() for s in soup('span')]
#print(soup)
#result = s.findAll("div",{"class","bbs-screen bbs-content"})
#for i in soup.findAll('span'): 
	#print(i)
#with open("./output2.txt", 'a') as out:
	#out.write(str(soup))
#print(result)