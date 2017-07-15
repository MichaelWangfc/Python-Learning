# !usr/bin/env python
# -*- coding:utf-8 -*-
__author__ = 'qionghui.zheng'

import requests
import json
import time
import pandas as pd
import sys
reload(sys)
sys.setdefaultencoding('utf8')

file_dict = 'dict.xlsx'
org_file = 'a1.xlsx'

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

result_pd['key'] = new_k
result_pd['value'] = new_v

print result_pd
result_pd.to_excel('result1.xlsx')












