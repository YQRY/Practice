# users/朔/PycharmProjects
# -*- coding:utf-8 -*-
# author:YQRY time:2018/9/29
import random
secret = random.randint(1,10)
times = 3
print('猜数小游戏')
guess = 0
print('猜我想的是哪个数字：', end='')
while (guess != secret) and (times > 0):
    temp = input()
    while not temp.isdigit():
        temp = input('抱歉，输入格式不对！请重输：')
    guess = int(temp)
    times = times - 1
    if guess == secret:
        print('牛逼！猜对了！')
    else:
        if guess > secret:
            print('大了')
        else:
            print('小了')
        if times > 0:
            print('再试一次吧:',end='')
        else:
            print('机会用光了！')
print('游戏结束！')

