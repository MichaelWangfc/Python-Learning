# -*- coding:utf-8 -*-
import requests
import json
import glob
import pandas as pd
import numpy as np
import time
import sys
reload(sys)
sys.setdefaultencoding('utf8')

url = 'http://114.215.185.227:8456/AD/LossInfo/lossSubmit?_dc=1498526640024&status=60'
headers = {'Accept': '*/*',
'Accept-Encoding':'gzip, deflate',
'Accept-Language':'zh-CN,zh;q=0.8',
'Connection':'keep-alive',
'Content-Length':'1102',
'Content-Type':'application/json',
'Cookie':'JSESSIONID=F914BAC5FC239F27E1B57BF172408DE8',
'Host':'114.215.185.227:8456',
'Origin':'http://114.215.185.227:8456',
'Referer':'http://114.215.185.227:8456/AD/',
'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.101 Safari/537.36',
'X-Requested-With':'XMLHttpRequest',
'_dc':'1498526640024'}

y = {'addressPlace': '',
 'auditName': '高康彪',
 'auditOpinion': '',
 'auditRemark': '',
 'auditTime': '',
 'auditUser': 301,
 'bailDate': '2016-11-29 13:50:39',
 'bailDate2': '',
 'bailer': '杭州财产分公司',
 'carMark': '沪AXW630',
 'caseCode': 'ZJ201706A000027',
 'chassisNo': '',
 'cmplextDesc': '',
 'complexState': '',
 'contactName': 'zhu',
 'contactPhone': '78945612',
 'department': '杭州营业部',
 'dispatchTime': '2016-11-29 13:50:39',
 'dispatcher': '王',
 'dispatcherId': 41,
 'docQuality': '',
 'enabled': 1,
 'end': 0,
 'guid': '7df7b4bb-3f3b-439f-8774-8b664d9b1ed1',
 'id': 4722,
 'insertTime': '2016-02-23 10:19:07',
 'isPhone': '',
 'isSubject': 2,
 'lastTime': '2016-02-24 09:33:56',
 'limit': 0,
 'lossAddress': '上海上海闵行区',
 'lossDesp': '未按规定让行',
 'lossQuality': '',
 'lossTime': '',
 'managementFee': '',
 'materialAmount': '',
 'modeId': '',
 'operater': '王',
 'page': 0,
 'recModiDate': '',
 'recModiId': '',
 'recModiOperId': '',
 'remnant': '',
 'repairFtName': '特约维修站',
 'repairFtPhone': '',
 'repairFtType': '',
 'reportNo': '1000009177',
 'start': 0,
 'subtotal': '',
 'subtractRate': '',
 'taskstate': '40',
 'userId': 41,
 'userName': '王',
 'vehicleModel': '宝马BMW7250 325i(08/12-12)',
 'vehicleNo': '',
 'vin': ''}

#df_oro = pd.read_excel('a3.xlsx')
#name_dic ={'车牌号':'carMark',
#'修理厂':'repairFtName',
#'出险地点':'lossAddress'}
#name_list = list(df_oro['key'])

#for i in name_list:
# if i in name_dic:
  #print name_dic[i]

#a=glob.glob('sixjia.xlsx')
#cc = pd.DataFrame()
#for i in a:
   # df = pd.read_excel(i)
   # cc = pd.concat([cc,df])
#c1 = cc[['车牌号','修理厂','出险地点']]
#c11=c1[c1['车牌号']!=1][['车牌号','修理厂','出险地点']]
#c11.columns = ['carMark','repairFtName','lossAddress']
file_dict = 'D:/My Documents/WeChat Files/wangfeicheng007/Attachment/dict.xlsx'
org_file = 'D:/My Documents/WeChat Files/wangfeicheng007/Attachment/a1.xlsx'

result_pd = pd.DataFrame(columns=['key', 'value'])
new_k, new_v = [], []

df_dict = pd.read_excel(file_dict,header=0)
chi_list = df_dict['chi']
eng_list = df_dict['eng']
name_dic = dict(zip(chi_list,eng_list))
#print json.dumps(name_dic, ensure_ascii=False)

df_file = pd.read_excel(org_file,header=0)
f_key = df_file['key']
f_value = df_file['value']
file_dict = dict(set(zip(f_key,f_value)))


for i in file_dict:
    if i in name_dic:
        new_k.append(name_dic[i])
        new_v.append(file_dict[i])

#result_pd['key'] = new_k
#result_pd['value'] = new_v

result=dict(zip(new_k,new_v))
print result

#print result_pd
#result_pd.to_excel('result.xlsx')

for i in result:
    y['carMark'] = result['carMark']
    y['repairFtName'] = result['repairFtName']
    y['lossAddress'] = result['lossAddress']
    y['vehicleModel'] = result['vehicleModel']
    requests.post(url,data=json.dumps(y),headers = headers)

requests.post(url,data = json.dumps(y),headers = headers )

url1='http://114.215.185.227:8456/AD/Part/add?_dc=1499157165536&guid=43e2450d-4213-4ddd-b56d-2061600040ca&lossId=4722'
headers1 = {'Accept':'*/*',
'Accept-Encoding':'gzip, deflate',
'Accept-Language':'zh-CN,zh;q=0.8',
'Connection':'keep-alive',
'Content-Length':'201',
'Content-Type':'application/json',
'Cookie':'JSESSIONID=F914BAC5FC239F27E1B57BF172408DE8',
'Host':'114.215.185.227:8456',
'Origin':'http://114.215.185.227:8456',
'Referer':'http://114.215.185.227:8456/AD/',
'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.101 Safari/537.36',
'X-Requested-With':'XMLHttpRequest',
'_dc':'1499157165536'}

qq = {'complexPrice': '',
'guid': "",
'insertTime': "",
'lossId': "",
'marketPrice': 20,
'partCode': "013311515A",
'partId': '',
'partName': "变速箱倒档轴",
'partNum': 1,
'reamrk': "",
'sPrice': ''}
for x in result:
    qq['partCode'] = result['partCode']
    qq['partName'] = result['partName']
    qq['partNum'] = result['partNum']
    qq['marketPrice'] = result['marketPrice']
    #requests.post(url1,data=json.dumps(qq),headers = headers1)

requests.post(url1,data = json.dumps(qq),headers = headers1 )




