# -*- coding=utf-8 -*-
import os

path = "F:/MUSIC"  # 目标路径

"""os.listdir(path) 操作效果为 返回指定路径(path)文件夹中所有文件名"""
filename_list = os.listdir(path)  # 扫描目标路径的文件,将文件名存入列表

a = 0
for i in filename_list:
    # print(filename_list[a].replace(" ", ""))
    used_name = path + "/" + filename_list[a]
    # print(used_name)
    new_name = filename_list[a].replace(" ", "")
    new_name = path + "/" + new_name
    try:
        os.rename(used_name, new_name)
    except Exception as e:
        # os.remove(used_name)
        print(e)

    print("文件%s重命名成功,新的文件名为%s" % (used_name, new_name))
    a += 1
