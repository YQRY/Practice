# users/朔/PycharmProjects
# -*- coding:utf-8 -*-
# author:YQRY time:2018/12/1
def is_palindrome(n, start, end):
    if start > end:
        return 1
    else:
        return is_palindrome(n, start+1, end-1) if n[start] == n[end] else 0

string = input('请输入一个字符：')
length = len(string)-1

if is_palindrome(string, 0, length):
    print('\"%s\"是回文字符串！' % string)
else:
    print('\"%s\"不是回文字符串！' % string)