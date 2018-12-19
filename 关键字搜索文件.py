# users/朔/PycharmProjects
# -*- coding:utf-8 -*-
# author:YQRY time:2018/12/10
import os

def print_pos(key_dict):
    keys = key_dict.keys()
    keys = sorted(keys)               #因为字典是无序的，这里对行数进行排序
    for each_key in keys:
        print('关键字出现在第 %s 行，第 %s 个位置' % (each_key, str(key_dict[each_key])))

def pos_in_line(line, key):
    pos = []
    begin = line.find(key)
    while begin != 1:
        pos.append(begin + 1)          #用户的角度是从1开始
        begin = line.find(key, begin+1)     #从下一个位置继续查找

    return pos

def search_in_file(file_name, key):
    f = open(file_name)
    count = 0
    key_dict = dict()               #字典，用户存放key所在行数对应具体位置

    for each_line in f:
        count += 1
        if key in each_line:
            pos = pos_in_line(each_line, key)     #key在每行对应的位置
            key_dict[count] = pos

    f.close()
    return key_dict


def search_files(key, detail):
    all_files = os.walk(os.getcwd())
    txt_files = []

    for i in all_files:
        for each_file in i[2]:
            if os.path.splitext(each_file)[1] == '.txt':        #根据后缀来判断是否文本文件
                each_file = os.path.join(i[0], each_file)
                txt_files.append(each_file)

                for each_txt_file in txt_files:
                    key_dict = search_in_file(each_txt_file, key)
                    if key_dict:
                        print('===============================================')
                        print('在文件【%s】中找到关键字【%s】' % (each_txt_file, key))
                        if detail in ['YES', 'Yes', 'yes']:
                            print_pos(key_dict)


key = input('请将该脚本放于待查找的文件内，请输入关键字：')
detail = input('是否需要打印关键字【%s】在文件中的具体位置(YSE/NO):' % key)
search_files(key, detail)