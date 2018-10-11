# users/朔/PycharmProjects
# -*- coding:utf-8 -*-
# author:YQRY time:2018/10/11
x = int(input('输入一个整数：'))
y = int(input('再输入一个整数：'))
small = x if x < y else y         #三元操作符，即ifx<y,small=x;else,small=y
print('较小的数是： ', small)
