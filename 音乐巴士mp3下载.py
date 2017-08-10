#!/usr/bin/env python
#-*-coding:utf-8 -*-

from urllib import request
import re           #正则表达式库
url="http://www.yy8844.cn/ting/mvovc/cciimc.shtml"

#发送http请求
response=request.urlopen(url)
html=response.read().decode('GBK')
music_id=int(re.findall(r'MusicId=(\d+)',html)[0])      #int()将字符串变为整数
music_name=re.findall(r'<title>(.*)</title>',html)[0].split('/')[0]

#拼接mp3_URL
music_url="http://96.ierge.cn/%d/%d/%s.mp3" % (music_id//30000,music_id//2000,music_id)
print("%s正在下载。。。"%music_name)
print(music_url)     #得到mp3下载链接
data=request.urlopen(music_url).read()
#下载mp3

#写mp3文件
with open("%s.mp3"% music_name,'wb') as f:
    f.write(data)

print("%s下载完成！"%music_name)

#下载歌词
def lrc():
    music_word0=re.findall(r'<div class="textgeci" id="showtext">(.*?)</div>',html,re.S)[0]
    music_word=music_word0.replace('<BR>','')
    print(music_word)
    with open('%s.txt' % music_name,'w') as f:
        f.write(music_word)
    print('%s歌词下载完成！'%music_name)

lrc_if=int(input("是否下载歌词（是请输入1）:"))
if lrc_if==1:
    lrc()
else:
    print('歌词未下载')
