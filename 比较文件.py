# users/朔/PycharmProjects
# -*- coding:utf-8 -*-
# author:YQRY time:2018/12/8
def file_compare(file1, file2):
    f1 = open(file1 )    #打开该程序所在文件夹内的文件
    f2 = open(file2)
    count = 0    #统计行数
    differ = []   #统计不一样的行数

    for line1 in f1:
        line2 = f2.readline()
        count += 1
        if line1 != line2:
            differ.append(count)

    f1.close()
    f2.close()
    return differ

file1 = input('请输入第一个文件名(带格式后缀)：')
file2 = input('请输入第二个文件名(带格式后缀)：')

differ = file_compare(file1, file2)

if len(differ) == 0:
    print('两个文件内容完全一样！')
else:
    print('两个文件共有【%d】处不同：' % len(differ))
    for each in differ:
        print('第 %d 行不一样' % each)
