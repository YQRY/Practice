# users/朔/PycharmProjects
# -*- coding:utf-8 -*-
# author:YQRY time:2018/10/25
def gcd(x, y):
    while y:
        t = x % y
        x = y
        y = t

    return x

print(gcd(4,6))