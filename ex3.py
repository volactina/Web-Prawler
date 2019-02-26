'''
在“http://money.cnn.com/data/dow30/”
上抓取道指成分股数据并将30家公司的代码、公司名称和最近一次成交价放到一个列表中输出
'''
import requests
from bs4 import BeautifulSoup
import re

r=requests.get('https://money.cnn.com/data/dow30/')
soup=BeautifulSoup(r.text,'lxml')
codes=soup.find_all('a','wsod_symbol')
pattern_names=re.compile('<span title="(.*?)">(.*?)<\/span>')
names=re.findall(pattern_names,r.text)
pattern_prices=re.compile('<span stream="last_(.*?)" class="wsod_stream">(.*?)<\/span>')
prices=re.findall(pattern_prices,r.text)
results=[]
for i in range(30):
    results.append(tuple((i+1,codes[i].string,names[i][1],prices[i][1])))
for result in results:
    print(result)