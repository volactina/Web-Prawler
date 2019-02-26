# Web-Prawler

程序清单

ex1

这段程序从豆瓣网上爬取了《百年孤独》的评论和得分

Coursera-《用python玩转数据》2.1.2（南京大学）

ex2

抽取某本书的前50条短评内容并计算评分的平均值.

提示：有的评论中并不包含评分

(这个问题没有解决，我觉得它的参考代码也没有解决这个问题）

ex3

在“http://money.cnn.com/data/dow30/”

上抓取道指成分股数据并将30家公司的代码、公司名称和最近一次成交价放到一个列表中输出

参考代码用了更精炼的正则表达式一次性提取了所有信息

# -*- coding: utf-8 -*-
"""

Retrieve dji stock data

@author: Dazhuang

"""

import requests

import re

def retrieve_dji_list():

    r = requests.get('http://money.cnn.com/data/dow30/')
    
    # put the re expression on one line and pay attention to the '\n'
    
    search_pattern = re.compile('class="wsod_symbol">(.*?)<\/a>.*?<span.*?">(.*?)<\/span>.*?\n.*?class="wsod_stream">(.*?)<\/span>')
    
    dji_list_in_text = re.findall(search_pattern, r.text)
    
    return dji_list_in_text

dji_list = retrieve_dji_list()

print(dji_list)
