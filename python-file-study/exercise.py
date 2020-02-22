#练习
# 练习一 文件的创建和使用
# 1. 创建一个文件，并写入当前日期
# 2. 再次打开这个文件，读取文件的前4个字符后退出
import datetime
file = open('txt.txt', 'w')
file.write(str(datetime.datetime.now()))
file.close()

file1 = open('txt.txt')
print(file1.read(4))
file1.close()