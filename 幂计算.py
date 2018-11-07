# users/朔/PycharmProjects
# -*- coding:utf-8 -*-
# author:YQRY time:2018/10/25
def power(x, y):
    result = 1

    for i in range(y):
        result *= x

    return result

print(power(2, 3))
