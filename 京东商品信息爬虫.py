#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/8/18 11:48
# @Author  : Jonas
# @Site    :
# @File    : 京东商品信息爬虫.py
# @Software: PyCharm
# @Verdion : 1.0

from multiprocessing.dummy import Pool as Thredpool
from lxml import etree
import time
import sys
import requests
import json
import pymongo


def get_response(url):
    html=requests.get(url,headers=headers)  #传参
    selector=etree.HTML(html.text)#解析html
    product_list=selector.xpath('//*[@id="J_goodsList"]/ul/li[3]')#xpath是解析网页的一种方法
    for product in product_list:
        try:
            sku_id=product.xpath('@data-sku')[0]
            product_url='https://item.jd.com/{}.html'.format(str(sku_id))
            get_data(product_url)
        except Exception as e:
            print(e)

def get_data(product_url):
    '''
    获取商品详情
    :param url:
    :return:
    '''
    product_dict={}
    html=requests.get(product_url,headers=headers)      #目的商品页面
    selector=etree.HTML(html.text)
    product_infos=selector.xpath('//ul[@class="parameter1 p-parameter-list"]')
    for product in product_infos:
        product_num=product.xpath('li[2]/@title')[0]
        product_price=get_product_price(product_num)        #商品编号就是sku
        product_dict['商品名称'] = product.xpath('li[1]/@title')[0]
        product_dict['商品编号'] = product_num
        product_dict['商品产地'] = product.xpath('li[4]/@title')[0]
        product_dict['商品价格'] = product_price
        print(product_dict)
    for items in product_dict.values():
        print(items)

    save(product_dict)

def get_product_price(sku):
    '''
    获取商品价格
    :return:
    '''
    price_url='https://p.3.cn/prices/mgets?skuIds=J_{}'.format(str(sku))
    response=requests.get(price_url,headers=headers).content
    response_json=json.loads(response)
    for info in response_json:
        return info.get('p')

def save(product_list):
    client=pymongo.MongoClient('localhost')
    db=client['product_dict']
    content=db['jd']
    content.insert(product_list)



if __name__=='__main__':
    headers={
        'User-Agent:Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.63 Safari/537.36 Qiyu/2.1.1.0'
        #伪装浏览器
    }

    urls = ['https://search.jd.com/Search?keyword=%E6%89%8B%E6%9C%BA&enc=utf-8&qrst=1&rt=1&stop=1&vt=2&cid2=653&cid3=655&page={}&s=56&click=0'.format(page) for page in (1,10,2) ]
    pool = Thredpool(2)
    start_time = time.time()
    pool.map(get_response,urls)
    pool.close()
    pool.join()
    end_time=time.time()
    print(u'用时{}秒'.format(str(end_time-start_time)))
