# users/朔/PycharmProjects
# -*- coding:utf-8 -*-
# author:YQRY time:2018/12/1
def hanoi(n, x, y, z):
    if n == 1:
        print(x, '-->', z)
    else:
        hanoi(n-1, x, z, y)    #先将上面的n-1个盘子从x借助z放到y上
        print(x, '-->', z)    #再将最下面一个盘子从x放到z上
        hanoi(n-1, y, x, z)   #最后y上的n-1个盘子从y借助x放到z上

n = int(input('请输入汉诺塔层数：'))
hanoi(n, 'x', 'y', 'z')