# users/朔/PycharmProjects
# -*- coding:utf-8 -*-
# author:YQRY time:2018/11/6
def mFun(*param, base=5):
    result = 0
    for each in param:
        result += each

    result *= base

    print('结果是：', result)

mFun(1, 2, 3, 7)