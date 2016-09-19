# -*- coding:utf-8 -*-
import urllib2
import re
from Simple_Spider.Tools import Tools
import sys


class BDTB:
    def __init__(self, url, see_lz):
        """
        see_lz：是否仅看楼主。1是看，0不看
        page_id：页码
        """
        self.index = 1  # 循环次数
        self.floor = 1  # 楼层
        self.url = url
        self.see_lz = see_lz
        #url = 'http://tieba.baidu.com/p/3138733512?see_lz=1&pn=1'

    def get_content(self, number):
        try:
            url_para = ''.join(('?see_lz=', str(self.see_lz), '&pn=', str(number)))
            url = ''.join((self.url, url_para))
            request = urllib2.Request(url)
            response = urllib2.urlopen(request)
        except urllib2.URLError, e:
            self.e_log(e)
        content = response.read().decode('utf-8')
        return content

    def get_total_page(self, content):
        reg = '<li class="l_reply_num".*?</span>.*?>(.*?)</span>'
        try:
            pattern = re.compile(reg, re.S)
            items = re.search(pattern, content)
        except Exception, e:
            self.e_log(e)
        if not items:
            raise Exception('内容为空')
        return int(items.group(1).strip())

    def get_title(self, content):
        reg = '<h3 class="core_title_txt.*?>(.*?)</h3>'
        try:
            pattern = re.compile(reg, re.S)
            items = re.findall(pattern, content)
        except Exception, e:
            self.e_log(e)
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
    def get_contents(content):
        reg = '<div id="post_content.*?j_d_post_content ">(.*?)</div>'
        pattern = re.compile(reg, re.S)
        items = re.findall(pattern, content)
        tool = Tools()
        contents = []
        for item in items:
            item = tool.replace(item)
            contents.append(item)
        return contents

    def write_data(self, contents):
        file_path = Tools.get_file_name(u'百度百科', 'BDTB')
        with open(file_path, 'a') as f:
            f.write('今日话题：%s' % self.get_title(content))
            for item in contents:
                f.write('\n' * 2)
                f.write('楼层：%d' % self.floor)
                f.write('\n')
                f.write(item)
                f.write('\n' * 2)
                f.write("*" * 30)
                f.write('\n' * 2)
                self.floor += 1


if __name__ == '__main__':
    reload(sys)
    sys.setdefaultencoding('utf-8')
    a = BDTB('http://tieba.baidu.com/p/3138733512', 1)
    content = a.get_content('1')
    page_amount = a.get_total_page(content)
    print '共%d页' % page_amount
    while a.index <= page_amount:
        print '正在写入第%d页...' % a.index
        content = a.get_content(a.index)
        contents = a.get_contents(content)
        a.write_data(contents)
        a.index += 1
    print '写入完成！！'





