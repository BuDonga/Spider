# -*- coding:utf-8 -*-
import re


class Tools:
    def __init__(self):
        self.replace_a = re.compile('<a.*?>|</a>', re.S)  # 删除a标签
        self.replace_img = re.compile('<img.*?>|</img>', re.S)  # 删除img图片
        self.replace_br = re.compile('<br><br><br><br>|<br><br><br>|<br><br>|<br>', re.S)  # 替换换行符
        self.replace_blank = re.compile('           |       |      |     ', re.S)  # 替换空格
        self.replace_para = re.compile('\n', re.S)  # 段落缩进

    def replace(self, content):
        try:
            content = re.sub(self.replace_a, '', content)
            content = re.sub(self.replace_img, '', content)
            content = re.sub(self.replace_br, '\n', content)
            content = re.sub(self.replace_blank, '', content)
            content = re.sub(self.replace_para, '\n\n    ', content)
        except Exception, e:
            print e.message
        return content.strip()
