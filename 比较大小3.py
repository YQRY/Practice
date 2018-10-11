# users/朔/PycharmProjects
# -*- coding:utf-8 -*-
# author:YQRY time:2018/10/11
x = int(input('输入第一个数：'))
y = int(input('输入第二个数：'))
z = int(input('输入第三个数：'))
small = x if(x < y and x < z) else (y if y < z else z)   # 三元操作符
print('最小的数是：', small)