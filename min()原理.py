# users/朔/PycharmProjects
# -*- coding:utf-8 -*-
# author:YQRY time:2018/10/25
def min(x):
    least = x[0]

    for each in x:
        if each < least:
            least = each

    return least

print(min('10234567'))