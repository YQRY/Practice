# users/朔/PycharmProjects
# -*- coding:utf-8 -*-
# author:YQRY time:2018/12/10
import os

def search_video(start_dir, target):
    os.chdir(start_dir)                 #将start_dir修改为当前工作路径

    for each_file in os.listdir(os.curdir):
        ext = os.path.splitext(each_file)[1]
        if ext in target:
            vedio_list.append(os.getcwd() + os.sep + '<<' + each_file + '>>' + os.linesep)
            #os.linesep：当前平台使用的行终止符（Win下为'\r\n'，Linux下为'\n'）

        if os.path.isdir(each_file):         #判断each_file是否存在且是一个目录
            search_video(start_dir,target)    #如果each_file是一个目录，采用递归法继续搜索
            os.chdir(os.pardir)              #将上一级目录修改为当前工作路径

start_dir = input('请输入待查找的初始目录：')
program_dir = os.getcwd()

target = ['.mp4', '.avi', 'rmvb']
vedio_list = []

search_video(start_dir, target)

f = open(program_dir + os.sep + 'vedioList.txt', 'w')      #创建一个文档来保存视频文件名
f.writelines(vedio_list)
f.close()