# users/朔/PycharmProjects
# -*- coding:utf-8 -*-
# author:YQRY time:2018/11/8
def fun(var):
    var = 1314
    print(var, end='')

var = 520        #此时的var与fun()函数体内的var不是同一个
fun(var)         #此时的var与fun()函数体内的var不是同一个
print(var)       #此时的var与fun()函数体内的var不是同一个