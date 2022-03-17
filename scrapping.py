# -*- coding: utf-8 -*-
import requests
import re
import threading
from urllib.parse import urlparse
from collections import defaultdict
from collections import Counter
import datetime


begin_time = datetime.datetime.now()
input=['news.ycombinator.com','reddit.com','w3shools.com']

def Find(data):
  
    # findall() has been used 
    # with valid conditions for urls in string
    regex = r"(?i)\b((?:https?://|www\d{0,3}[.]|[a-z0-9.\-]+[.][a-z]{2,4}/)(?:[^\s()<>]+|\(([^\s()<>]+|(\([^\s()<>]+\)))*\))+(?:\(([^\s()<>]+|(\([^\s()<>]+\)))*\)|[^\s`!()\[\]{};:'\".,<>?«»“”‘’]))"
    url = re.findall(regex,data)
    lst=[]
    for x in url:
    	val=urlparse(x[0]).netloc
    	if len(val) >=5:
    		lst.append(val)
    return lst

x=[]
data=""

for url in input:
    print('http://'+url)
    response = requests.get('http://'+url)
    data+=response.content.decode('utf-8')
x=(Find(data))
c = Counter(x)
print(c.most_common(5))
execution_time = datetime.datetime.now()-begin_time
print(execution_time)