# -*- coding:utf-8 -*-
import urllib2
import urllib
import re
import sys
import os
import HTMLParser

reload(sys)
sys.setdefaultencoding('utf-8')
page = 6
url = ''.join(('http://www.qiushibaike.com/8hr/page/', str(page)))
user_agent = 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/46.0.2490.86 Safari/537.36'
headers = {'User-Agent': user_agent}

try:
    request = urllib2.Request(url, headers=headers)
    response = urllib2.urlopen(request)
except urllib2.URLError, e:
    if hasattr(e, 'code'):
        print e.code
    elif hasattr(e, 'reason'):
        print e.reason

content = response.read().decode('utf-8')
regular = '<div class="article block.*?<a href.*?title.*?<h2>(.*?)</h2>.*?<div.*?Gender(.*?)">(.*?)</div>.*?<span>' \
          '(.*?)</span>.*?number">(.*?)</i>.*?number">(.*?)</i>'
pattern = re.compile(regular, re.S)
items = re.findall(pattern, content)
a = []
index = 1
with open(u'..\\糗事百科\\糗事百科.txt', 'a') as f:
    for item in items:
        item = list(item)
        if item not in a:
            for b in range(0,5):
                item[b] = HTMLParser.HTMLParser().unescape(item[b]).encode()  # 处理HTML转义字符
            # print item[0]  # 用户
            # print item[1]  # 性别Icon
            # print item[2]  # 年龄
            # print item[3]  # 段子内容
            # print item[4]  # 赞
            # print item[5]  # 评论数
            item[3] = item[3].replace('<br/>', '\n')
            a.append(item)
            f.write('No.%d\n' %index)
            f.write('用户：%s\n' %item[0])
            if 'woman' in item[1]:
                f.write('性别：女\n')
            else:
                f.write('性别：男\n')
            f.write('年龄：%s\n' %item[2])
            f.write('获赞：%s\n' %item[4])
            f.write('评论数：%s\n' %item[5])
            f.write(u'段子内容：\n')
            f.write(item[3])
            f.write('\n'*2)
            f.write('-'*30)
            f.write('\n' * 2)
            index += 1

