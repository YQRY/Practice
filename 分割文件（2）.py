# users/朔/PycharmProjects
# -*- coding:utf-8 -*-
# author:YQRY time:2018/12/7
def save_file(boy, girl, count):            #将save操作封装为一个函数，下面直接调用
    boy_file_name = 'boy_' + str(count) + '.txt'    #设置文件名取名方式
    girl_file_name = 'girl_' + str(count) + '.txt'

    boy_file = open(boy_file_name, 'w')      #以写入方式打开文件
    girl_file = open(girl_file_name , 'w')

    boy_file.writelines(boy)               #将内容按行写入文件
    girl_file.writelines(girl)

    boy_file.close()                       #关闭文件
    girl_file.close()

def split_file(file_name):                   #将split操作封装为一个函数，方面直接调用
    f = open('D:\学习\研究生\python资料\Test\文件\\record.txt')

    boy = []                           #定义空的集合
    girl = []
    count = 1                          #计数变量的初始值为1

    for each_line in f:               #一行一行的提取文件内容
        if each_line[:6] != '======':      #以‘====’为分界线来分割文件
            (role, line_spoken) = each_line.split(':', 1)     #将每一行内容按照‘：’分为两部分
            if role == '小甲鱼':            #如果每行语句前面是‘小甲鱼’，将冒号后面的内容添加到boy文件中
                boy.append(line_spoken)
            if role == '小客服':             #同上
                girl.append(line_spoken)
        else:
            save_file(boy, girl, count)      #与到‘====’则将之前的内容保存到boy，girl文件中

            boy = []         #初始化boy文件
            girl = []        #初始化girl文件
            count += 1

    save_file(boy, girl, count)         #循环结束后，保存最后一个分界线‘====’下面的内容

    f.close()              #关闭文件，这样写入的内容才能缓存到各个小文件中

split_file('D:\学习\研究生\python资料\Test\文件\\record.txt')        #测试‘record’文件
