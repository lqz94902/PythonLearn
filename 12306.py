#coding=utf-8  

import urllib2 
import ssl
import re
from json import loads            #json转字典

ssl._create_default_https_context =ssl._create_unverified_context       #忽略SSL证书错误
from_station="ZUS"
to_station="TNS"
#漳州-泰宁
def getlist():
    response = urllib2.urlopen('https://kyfw.12306.cn/otn/leftTicket/query?leftTicketDTO.train_date=2017-08-12&leftTicketDTO.from_station=ZUS&leftTicketDTO.to_station=TNS&purpose_codes=ADULT') 
    html = response.read() 
    print type(html)
    print html
    dict=loads(html)
    print type(dict)
     
getlist()
#数据提取未处理
