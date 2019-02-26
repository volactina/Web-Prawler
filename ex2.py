'''
抽取某本书的前50条短评内容并计算评分的平均值.
提示：有的评论中并不包含评分
(这个问题没有解决，我觉得它的参考代码也没有解决这个问题）
'''
import requests
from bs4 import BeautifulSoup
import re

cnt=0
i=1
while cnt<50:
    r=requests.get('https://book.douban.com/subject/6082808/comments/hot?p='+str(i))
    soup=BeautifulSoup(r.text,'lxml')
    comments=soup.find_all('span','short')
    k=cnt
    for item in comments:
        cnt+=1
        print(cnt,'.',item.string)
        if(cnt==50):
            break
    pattern_s=re.compile('<span class="user-stars allstar(.*?) rating"')
    p=re.findall(pattern_s,r.text)
    sum=0
    for star in p:
        k+=1
        print(k,'.',star)
        sum+=int(star)
    print(sum)
    i+=1