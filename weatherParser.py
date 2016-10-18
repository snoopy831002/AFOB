import urllib.request
from urllib.request import urlopen


#correct parser code
apikey = 'CWB-335DC393-FCA8-4D15-9856-7AF060E0C210'
data = 'F-D0047-079'
requestURL = 'http://opendata.cwb.gov.tw/opendataapi?dataid=F-D0047-077&authorizationkey=CWB-335DC393-FCA8-4D15-9856-7AF060E0C210' 
root = urllib.request.urlopen(requestURL)
s=root.read()
print(s)
#correct parser code
