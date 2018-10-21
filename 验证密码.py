# users/朔/PycharmProjects
# -*- coding:utf-8 -*-
# author:YQRY time:2018/10/15
count = 3
password = '巴扎黑'

while count:
    pd = input('请输入密码：')
    if pd == password:
        print('密码正确，进入程序！')
        break
    elif '*' in pd:
        count -= 1        #自改
        print('密码中不能含有"*"号！您还有', count, '次机会！',end = '')
        continue
    else:
        count -= 1       #自改
        print('密码输入错误！您还有', count, '次机会！',end='')
