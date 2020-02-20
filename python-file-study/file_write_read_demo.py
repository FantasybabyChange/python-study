import os
# 文件读写
file1 = open("name.txt", 'w')
file1.write('中文')
file1.close()

file2 = open("name.txt", 'a')
file2.write('\n 新中文--')
# 一定要close
file2.close()

file3 = open("name.txt")
size = os.path.getsize("name.txt")
print(size)
file3.seek(0)
print('---'+file3.read())

file3.close()
