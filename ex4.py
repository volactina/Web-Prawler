'''
请爬取网页
http://www.volleyball.world/en/vnl/women/results-and-ranking/round1
上的数据（包括TEAMS and TOTAL, WON, LOST of MATCHES）

提示：
在处理时可以用已学的方法将每一项需要的内容（如USA和15）单独解析出来，
但这种做法将有联系的数据打散了，较好的做法是将每个TEAM的相关数据按组解析出来。
但是由于包含这4项信息的源代码（请自行观察）分在多行并且行首有多个空格，
因此在处理时在构造正则表达式时要把换行时的空白字符表示出来
（用\s+可表示多个空白字符，包括换行符和空格）。
'''
import requests
import re

r=requests.get('http://www.volleyball.world/en/vnl/women/results-and-ranking/round1')
pattern=re.compile('<figcaption><a id="(.*?)" href="(.*?)">(.*?)<\/a><\/figcaption>\s+<\/figure>\s+<\/td>\s+<td>(.*?)<\/td>\s+<td class="table-td-bold">(.*?)<\/td>\s+<td class="table-td-rightborder">(.*?)<\/td>')
lst=re.findall(pattern,r.text)
for i in range(len(lst)):
    lst[i]=lst[i][2:6]
    print(lst[i])