# users/朔/PycharmProjects
# -*- coding:utf-8 -*-
# author:YQRY time:2018/11/8
def palindrome(string):              #疑问
    length = len(string)
    last = length-1
    length //= 2
    flag = 1
    for each in range(length):
        if string[each] != string[last]:
            flag = 0
        last -= 1

    if flag == 1:
        return 1
    else:
        return 0

string = input('请输入一句话：')
if palindrome(string) ==  1:
    print('是回文联！')
else:
    print('不是回文联！')