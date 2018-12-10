# users/朔/PycharmProjects
# -*- coding:utf-8 -*-
# author:YQRY time:2018/12/8
def file_view(file_name, line_num):
    print('\n文件%s的前%s行的内容如下：\n' % (file_name, line_num))
    f = open(file_name)
    for i in range(int(line_num)):
        print(f.readline(), end = '')

    f.close()

file_name =  input(r'请输入文件名(带格式后缀)：')
line_num = input('请输入行数：')
file_view(file_name,line_num)
