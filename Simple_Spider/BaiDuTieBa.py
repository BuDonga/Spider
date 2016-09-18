# -*- coding:utf-8 -*-
import urllib2
import re
from Simple_Spider.Tools import Tools
import sys


class BDTB:
    def __init__(self, url, see_lz, page_id):
        """
        see_lz：是否仅看楼主。1是看，0不看
        page_id：页码
        """
        url_para = ''.join(('?see_lz=', str(see_lz), '&pn=', str(page_id)))
        r_url = ''.join((url, url_para))
        self.url = r_url
        #url = 'http://tieba.baidu.com/p/3138733512?see_lz=1&pn=1'

    def get_content(self):
        try:
            request = urllib2.Request(self.url)
            response = urllib2.urlopen(request)
        except urllib2.URLError, e:
            BDTB.e_log(e)
        content = response.read().decode('utf-8')
        return content

    @staticmethod
    def get_title(content):
        reg = '<h3 class="core_title_txt.*?>(.*?)</h3>'
        try:
            pattern = re.compile(reg, re.S)
            items = re.findall(pattern, content)
        except Exception, e:
            BDTB.e_log(e)
        if not items:
            raise Exception('内容为空')
        for item in items:
            title = item
        return title

    @staticmethod
    def e_log(e):
        if hasattr(e, 'code'):
            print e.code
        elif hasattr(e, 'message'):
            print e.message

    @staticmethod
    def load_page(content):
        reg = '<div id="post_content.*?j_d_post_content ">(.*?)</div>'
        pattern = re.compile(reg, re.S)
        items = re.findall(pattern, content)
        tool = Tools()
        index = 1
        with open(r'D:\Spider\BDTB\111.txt', 'w') as f:
            f.write('今日话题：%s' % BDTB.get_title(content))
            for item in items:
                item = tool.replace(item)
                print item
                print '-'*30
                f.write('\n'*2)
                f.write('楼层：%d' % index)
                f.write('\n')
                f.write(item)
                f.write('\n'*2)
                f.write("*"*30)
                f.write('\n'*2)
                index += 1


if __name__ == '__main__':
    reload(sys)
    sys.setdefaultencoding('utf-8')
    a = BDTB('http://tieba.baidu.com/p/3138733512', 1, 2)
    cont = a.get_content()
    b = a.get_title(cont)
    a.load_page(cont)
    # a = r'<a class="BDE_Image" src="http://im">迈卡威</a>TTTTTTTT<br>'
    # b = Tools(a)
    # print b.replace()


