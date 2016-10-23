import requests
import xmltodict
import json
from bs4 import BeautifulSoup
import dateutil.parser
t1=dateutil.parser.parse(str("2016-10-23T13:00:00+08:0"))
developerAuthkey='CWB-A2AE7398-BAE2-480E-961B-4B6D8F654F10'
cityId='F-D0047-077'
requestURL = 'http://opendata.cwb.gov.tw/opendataapi?dataid='+cityId+'&authorizationkey='+developerAuthkey
r = requests.get(requestURL)
paragraphs = """"""
if r.status_code == 200:
	soup = BeautifulSoup(r.text,"html.parser")
	s=soup.findAll("location")
	for letter in s:
		paragraphs+=str(letter)
	o = xmltodict.parse("<tainan>"+paragraphs+"</tainan>")
	with open("./output2.txt", 'a') as out:
		out.write("<tainan>"+paragraphs+"</tainan>")
	#print(json.dumps(o, indent=4, sort_keys=True))
	for index, item in enumerate(o['tainan']['location']):
		if(o['tainan']['location'][index]['locationname']=='北區'):
			break
	for index2, item2 in enumerate(o['tainan']['location'][index]['weatherelement'][9]['time']): 
		if(dateutil.parser.parse(str(o['tainan']['location'][index]['weatherelement'][9]['time'][index2]['starttime']))<=t1<=dateutil.parser.parse(str(o['tainan']['location'][index]['weatherelement'][9]['time'][index2]['endtime']))):
			print(o['tainan']['location'][index]['weatherelement'][9]['time'][index2]['elementvalue']['value'])
			break
		else:
			print('unable to find')
else:
	r.raise_for_status()



