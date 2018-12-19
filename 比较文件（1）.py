# users/朔/PycharmProjects
# -*- coding:utf-8 -*-
# author:YQRY time:2018/12/15
def file_compare(file1, file2):
    with open(file1 ) as f1, open(file2) as f2:     #利用with语句同时打开两个文件
        count = 0
        differ = []

        for line1 in f1:
            line2 = f2.readline()
            count += 1
            if line1 != line2:
                differ.append(count)
                                                 #因为with语句会自动关闭文件，所以此处不需要f.close()
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