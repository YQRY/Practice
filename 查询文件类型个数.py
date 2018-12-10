# users/朔/PycharmProjects
# -*- coding:utf-8 -*-
# author:YQRY time:2018/12/9
import os

all_files = os.listdir(os.curdir)     #列举当前目录中的文件名
type_dict = dict()                    #创建一个空的字典

for each_file in all_files:
    if os.path.isdir(each_file):      #判断每个文件是否存在且是一个目录
        type_dict.setdefault('文件夹', 0)   #如果文件类型是文件夹，则其作为键所对应的值为0，把文件类型和其值加入字典中
        type_dict['文件夹'] += 1            #文件夹作为键所对应的值加1，即文件类型的个数
    else:
        ext = os.path.splitext(each_file)[1]    #分离每个文件的文件名与拓展名，并提取拓展名
        type_dict.setdefault(ext, 0)            #如果文件类型不是文件夹，则其键所对应的值为0，把文件类型和其值加入字典中
        type_dict[ext] += 1                     #文件类型的值加1，即文件类型的个数

for each_type in type_dict.keys():              #提取字典中的每个键值
    print('该文件夹下共有类型为【%s】的文件 %d 个' % (each_type, type_dict[each_type]))