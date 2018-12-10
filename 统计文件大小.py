# users/朔/PycharmProjects
# -*- coding:utf-8 -*-
# author:YQRY time:2018/12/10
import os

all_files = os.listdir(os.curdir)
file_dict = dict()              #建立一个空的字典存储数据

for each_file in all_files:
    if os.path.isfile(each_file):
        file_size = os.path.getsize(each_file)
        file_dict[each_file] = file_size          #把每个文件的大小赋给对应的文件名

for each in file_dict.items():           #items()返回整个像的引用
    print('%s的大小是  [%dBytes]' % (each[0], each[1]))