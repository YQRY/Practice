# users/朔/PycharmProjects
# -*- coding:utf-8 -*-
# author:YQRY time:2018/12/14
import random
secret = random.randint(1, 10)
print('猜数小游戏')
temp = input('猜我想的是那个数：')
try:                                  #采用try...except异常处理机制，当输入的数不是整数时，自动提醒
    guess = int(temp)
except ValueError:
    print('输入错误！请输入整数！')
    guess = secret                 #为什么要加入这一步？？？
while guess != secret:
    temp = input('猜错了，再猜：')
    try:                            #再次采用try...except异常处理机制
     guess = int(temp)
    except ValueError:
        print('输入错误！请输入整数！')
    if guess == secret:
        print('牛逼！猜对了！')
    else:
        if guess > secret:
            print('大了')
        else:
            print('小了')
print('游戏结束！')
