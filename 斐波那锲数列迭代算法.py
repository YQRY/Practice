# users/朔/PycharmProjects
# -*- coding:utf-8 -*-
# author:YQRY time:2018/11/30
def fab(n):
    n1 = 1
    n2 = 1
    n3 = 1
    if n < 1:
        print('输入错误！')
        return -1

    while (n - 2) > 0:
        n3 = n1 + n2
        n1 = n2
        n2 = n3
        n -= 1

    return n3
result = fab(8)
if result != -1:
    print("总共有%d对小兔崽子出生！" % result)    #迭代算法速度快，但是逻辑思想难理解