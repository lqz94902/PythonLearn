#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/8/26 20:40
# @Author  : Jonas
# @Site    : 
# @File    : 2017年8月26日.py
# @Software: PyCharm
# @Version : 1.0

import random
# from tkinter import *
# Tk().mainloop()

dict_computer={
    1:'剪刀',
    2:'石头',
    3:'布'
}

dict_user={
    '剪刀':1,
    '石头':2,
    '布':3
}

while 1:
    rand = random.randint(1, 3)
    i=input('请输入：')
    if (i not in dict_computer.values()):
        print('请输入正确参数')
        continue
    num=dict_user[i]        #数字

    if(num==rand):
        print('电脑出也{},平局'.format(dict_computer[rand]))
    elif((num-rand)==1 or (num-rand)==-2):
        print('电脑出{},你赢了'.format(dict_computer[rand]))
    else:
        print('电脑出{},你输了'.format(dict_computer[rand]))
