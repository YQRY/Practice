# users/朔/PycharmProjects
# -*- coding:utf-8 -*-
# author:YQRY time:2018/10/25
def sum(x):
    result = 0

    for each in x:
        if (type(each) == int) or (type(each) == float):
            result += each
        else:
            continue

    return result

print(sum([1, 2.1, 2.3, 'a', '1', True]))