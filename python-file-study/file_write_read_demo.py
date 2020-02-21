import os
# 文件读写
file1 = open("name.txt", 'w')
file1.write('abcd')
file1.close()

file2 = open("name.txt", 'a')
file2.write('\n efgh--')
# 一定要close
file2.close()

file3 = open("name.txt")
size = os.path.getsize("name.txt")
print(size)

print('---'+file3.read(6))

file3.close()
