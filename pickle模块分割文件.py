# users/朔/PycharmProjects
# -*- coding:utf-8 -*-
# author:YQRY time:2018/12/13
import pickle

def save_file(boy, girl, count):
    boy_file_name = 'boy_' + str(count) + '.txt'
    girl_file_name = 'girl_' + str(count) + '.txt'

    boy_file = open(boy_file_name, 'wb')
    girl_file = open(girl_file_name , 'wb')

    pickle._dump(boy, boy_file)            #除了这一步，其他的都和分割文件(2)一样，这里采用（接下行）
    pickle._dump(girl, girl_file)          #pickle模块将文件boy,girl数组写入文件中

    boy_file.close()
    girl_file.close()

def split_file(file_name):
    f = open(file_name)

    boy = []
    girl = []
    count = 1

    for each_line in f:
        if each_line[:6] != '======':
            (role, line_spoken) = each_line.split(':', 1)
            if role == '小甲鱼':
                boy.append(line_spoken)
            if role == '小客服':
                girl.append(line_spoken)
        else:
            save_file(boy, girl, count)

            boy = []
            girl = []
            count += 1

    save_file(boy, girl, count)

    f.close()

split_file('D:\学习\研究生\python资料\练习代码（Github上传库）\\record.txt')