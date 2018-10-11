# users/朔/PycharmProjects
# -*- coding:utf-8 -*-
# author:YQRY time:2018/10/11
x = int(input('输入第一个数：'))
y = int(input('输入第二个数：'))
z = int(input('输入第三个数：'))
if x < y:             # x < y
    small = x         #接着比较x和z
    if z < small:     # z < x  如果small<z，small=small，所以不写small<z
        small = z     #所以z最小
elif y < z:           #y < x, 所以此时默认small=y，故比较y和z即(y < z)
    small = y         #所以y最小
else:
    small = z         #y < x, z < y
print('最小的数是：', small)  #理解比较数值思想和比较顺序