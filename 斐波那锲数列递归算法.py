# users/朔/PycharmProjects
# -*- coding:utf-8 -*-
# author:YQRY time:2018/11/30
def fab(n):
    if n < 1:
        print('输入错误！')
        return -1

    if n == 1 or n == 2:
        return 1
    else:
        return fab(n-1) + fab(n-2)

result = fab(8)
if result != -1:
    print("总共有%d对小兔崽子出生！" % result)   #递归算法计算较慢，但是逻辑思想容易理解