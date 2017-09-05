#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/8/27 20:17
# @Author  : Jonas
# @File    : 2017年8月27日.py
# @Software: PyCharm
# @Version : 1.3

import re
import requests
import sys
from urllib import request


def save():
    url='http://www.neihan8.com/article/index'+pw+'.html'
    print(url)
    response=request.urlopen(url)
    html=response.read().decode('utf-8')

    pattern_title=re.compile(r'">(.*?)</a></h3>')
    title=pattern_title.findall(html)

    pattern_item=re.compile(r'<div class="desc">(.*?)</div>')
    item=pattern_item.findall(html)

    with open('第{}页.txt'.format(pn),'w')as f:
        for j in item:
            f.write(j+'\n')

    print('第{}页下载完成'.format(pn))

if __name__=='__main__':
    pn_start=int(input('请输入起始页码:'))
    pn_end=int(input('请输入结束页码:'))
    for pn in range(pn_start,pn_end+1):
        if pn==1:
            pw=''
            save()
        else:
            pw='_{}'.format(pn)
            save()
