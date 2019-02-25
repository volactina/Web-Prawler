'''
这段程序从豆瓣网上爬取了《百年孤独》的评论和得分
'''
import requests
from bs4 import BeautifulSoup
import re

r=requests.get('https://book.douban.com/subject/6082808/comments/')
soup=BeautifulSoup(r.text,'lxml')
pattern=soup.find_all('span','short')
for item in pattern:
    print(item.string)
pattern_s=re.compile('<span class="user-stars allstar(.*?) rating"')
p=re.findall(pattern_s,r.text)
sum=0
for star in p:
    sum+=int(star)
print(sum)