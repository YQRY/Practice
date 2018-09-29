# users/朔/PycharmProjects
# -*- coding:utf-8 -*-
# author:YQRY time:2018/9/29
import random
secret = random.randint(1, 10)
print('猜数小游戏')
temp = input('猜我想的是那个数：')
guess = int(temp)
while guess != secret:
    temp = input('猜错了，再猜：')
    guess = int(temp)
    if guess == secret:
        print('牛逼！猜对了！')
    else:
        if guess > secret:
            print('大了')
        else:
            print('小了')
print('游戏结束！')


