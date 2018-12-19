# users/朔/PycharmProjects
# -*- coding:utf-8 -*-
# author:YQRY time:2018/12/10
import os

def search_file(start_dir, target):
    os.chdir(start_dir)               #将start_dir修改为当前工作路径

    for each_file in os.listdir(os.curdir):
        if each_file == target:
            print(os.getcwd() + os.sep + each_file)
        if os.path.isdir(each_file):
            search_file(each_file, target)       #迭代法继续搜索文件
            os.chdir(os.pardir)             #改变路径，返回上一级目录

start_dir = input('请输入待查找的初始目录：')
target = input('请输入待查找的目标文件：')
search_file(start_dir, target)