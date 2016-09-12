# -*- coding:utf-8 -*-
import urllib2
import urllib
import re
import  sys

reload(sys)
sys.setdefaultencoding( "utf-8" )
page = 2
url = ''.join(('http://www.qiushibaike.com/hot/page/', str(page), '/?s=4912246'))
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
#regular = '<div class=.*?author clearfix.*?<a href=.*?title=(.*?)>.*?manIcon">(.*?)</div>.*?<span>(.*?)</span>.*?"number">(.*?)</i>.*?</div></div>'
regular = 'title="(.*?)">'
pattern = re.compile(regular, re.S)
items = re.findall(pattern, content)
# for item in items:
#     print item[0]
for item in items:
    a = []
    if item not in a:
        a.append(item.decode())
    print a
