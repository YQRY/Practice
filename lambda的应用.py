# users/朔/PycharmProjects
# -*- coding:utf-8 -*-
# author:YQRY time:2018/11/29
def make_repeat(n):
    return lambda x : x * n

test = make_repeat(3)
print(test(5))
print(test('Good'))