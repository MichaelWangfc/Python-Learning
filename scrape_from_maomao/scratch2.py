import requests
import json
from bs4 import BeautifulSoup
url = 'http://114.80.84.22/MAS/chakan.do?o=getObj&taskNo=RDDH320150000004354037'
headers = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36'}
r = requests.get('http://114.80.84.22/MAS/chakan.do?o=getLogin&name=GS60000001&psd=TPIC01001a123456')
rr = requests.get(url,headers = headers,cookies = r.cookies)
ss = BeautifulSoup(rr.text,'lxml')
print ss
#a1 = a2 = []
#a = []
a1 = []
a2 = []
for news in ss.find_all('table'):
    slen1=len(news.find_all('th'))
    slen2=len(news.find_all('td'))
    if slen1<slen2:
        slen2=slen1
    for i in range(slen2):
        b1=news.find_all('th')[i].text.replace('\n','').replace('\r','').replace('\t','')
        b2 = news.find_all('td')[i].text.replace('\n', '').replace('\r', '').replace('\t', '')
        b3 = b1 + ":"+b2
        #print b3
        #a.append(b3)
        a1.append(b1)
        a2.append(b2)


import pandas as pd
#a1=pd.DataFrame(a)
#a1.to_excel('a1.xlsx')

print type(a1)
df = pd.DataFrame(columns=['key','value'])

df['key'] = a1
df['value'] = a2
df.to_excel('a1.xlsx')


