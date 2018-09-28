# users/朔/PycharmProjects
# -*- coding:utf-8 -*-
# author:YQRY time:2018/9/28
print("猜数小游戏")
temp = input("猜我想的是哪个数：")
guess = int(temp)
while guess != 8:
    temp = input("猜错了，再猜：")
    guess = int(temp)
    if guess == 8:
        print("牛逼！猜对了！")
    else:
        if guess > 8:
            print("大了")
        else:
            print("小了")
print("游戏结束！")