# users/朔/PycharmProjects
# -*- coding:utf-8 -*-
# author:YQRY time:2018/12/1
def Dec2Bin(dec):
    result = ''

    if dec:
        result = Dec2Bin(dec//2)
        return result + str(dec%2)
    else:
        return result

dec = int(input('请输入一个整数：'))
print(Dec2Bin(dec))