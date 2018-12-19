# users/朔/PycharmProjects
# -*- coding:utf-8 -*-
# author:YQRY time:2018/12/19
import random
import easygui as g

g.msgbox('欢迎来到猜数小游戏！')
secret = random.randint(1, 10)

msg = "猜我想的是那个数(1-10):"
title = "数字小游戏"
guess = g.integerbox(msg, title, lowerbound=1, upperbound=10)
#integerbox(msg = ”, title = ”, default = ”, lowerbound = 0, upperbound = 99, image = None, root = None, **invalidKeywordArguments)
#为用户提供一个简单的输入框，用户只能输入范围内（lowerbound参数设置最小值，upperbound参数设置最大值）的整型数值 ，否则会要求用户重新输入。

while True:
    if guess == secret:
        g.msgbox('猜中了，好厉害！')
        break
    else:
        if guess > secret:
            g.msgbox('大了')
        else:
            g.msgbox('小了')
        guess = g.integerbox(msg, title, lowerbound=1, upperbound=10)

g.msgbox('游戏结束！')