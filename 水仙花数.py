# users/朔/PycharmProjects
# -*- coding:utf-8 -*-
# author:YQRY time:2018/10/15
for i in range(100,1000):
    sum = 0
    temp = i
    while temp:
        sum = sum + (temp%10) ** 3      #取余
        temp //= 10                     #地板除
    if sum == i:
        print(i)