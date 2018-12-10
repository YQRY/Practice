# users/朔/PycharmProjects
# -*- coding:utf-8 -*-
# author:YQRY time:2018/12/8
def file_replace(file_name, rep_word, new_word):
    f_read = open(file_name)

    content = []
    i = 0
    time = 0

    for eachline in f_read:        #在for in ：文件中一行一行的返回语句
        if rep_word in eachline:
            i = eachline.count(rep_word)    #返回rep_word在每一行出现的次数
            time += i                       #返回rep_word在出现的总次数
            eachline = eachline.replace(rep_word, new_word)  #把rep_word替换为new_word
        content.append(eachline)

    decide = input('\n文件 %s 中共有%s 个【%s】\n您确定要把所有的【%s】替换为【%s】吗？\n【Yes/No】:' \
                   % (file_name, time, rep_word, rep_word, new_word))    #每一个%s对应后面相应位置的参数

    if decide in ['YEs', 'Yes', 'yes']:
        f_write = open(file_name, 'w')
        f_write.writelines(content)
        f_write.close()

    f_read.close()

file_name = input('请输入文件名：')
rep_word = input('请输入需要替换的单词或字符：')
new_word = input('请输入新的单词或字符：')
file_replace(file_name, rep_word, new_word)

