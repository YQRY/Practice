# users/朔/PycharmProjects
# -*- coding:utf-8 -*-
# author:YQRY time:2018/12/15
print('欢迎进入通讯录程序！')
print('1:查询联系人资料')
print('2:插入新的联系人')
print('3:删除已有联系人')
print('4：退出通讯录程序')

contacts = dict()

while True:
    instr = int(input('\n请输入相关的指令代码：'))

    if instr == 1:
        name = input('请输入联系人姓名：')
        try:                                         #利用try语句处理异常，可以避开每次都需要使用in判断键是否
            print(name + ':' + contacts[name])       #存在字典中中的操作。因为只要当键不存在字典中时，就会触
        except KeyError:                             #发KeyError异常，从而打印出要提示的内容
            print('您输入的姓名不在通讯录中！')

    if instr == 2:
        name = input('请输入联系人姓名：')
        try:                                                     #利用try语句处理异常...
            print('您输入的姓名在通讯录中已存在 -->>', end='')
            print(name + ':' + contacts[name])
            if input('是否修改用户资料（YES/NO）:') == 'YES':
                contacts[name] = input('请输入用户联系电话：')
        except KeyError:
            contacts[name] = input('请输入用户联系电话：')

    if instr == 3:
        name = input('请输入联系人姓名：')
        try:                                                  #利用try语句处理异常...
            del(contacts[name])
            print('已删除联系人%s的资料！' % name)
        except KeyError:
            print('您输入的联系人不存在！')

    if instr == 4:
        break

print('感谢使用通讯录！')

#使用条件语句虽然直观明了，但是效率不高。因为程序会两次访问字典的键，一次判断是否存（例如：if name in contacts），
# 一次获得值（例如：print(name + ':' + contacts[name])）。所以利用异常解决方案（with语句）处理更好