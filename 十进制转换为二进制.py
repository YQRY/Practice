# users/朔/PycharmProjects
# -*- coding:utf-8 -*-
# author:YQRY time:2018/10/25
def Dec2Bin(dec):
    temp = []
    result = ''

    while dec:
        quo = dec % 2
        dec = dec // 2
        temp.append(quo)

    while temp:
        result += str(temp.pop())

    return result

dec = int(input('请输入一个整数：'))
print(Dec2Bin(dec))
