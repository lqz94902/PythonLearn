#!/usr/bin/env python
#-*-coding:utf-8 -*-
import json

with open("Lib.txt" , "rt" ,encoding = "UTF-8") as file :
	word = eval(file.read())
print('词库初始化完毕！请输入单词')
while 1 :
	w = input()
	if w in word.keys() :
		print(word[w])
	else :
		print('未找到此单词！')
