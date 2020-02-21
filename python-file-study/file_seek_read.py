import os
file3 = open("name.txt")
size = os.path.getsize("name.txt")
print(size)

print(file3.read(2))
file3.seek(2, 0)
print(file3.tell())
print(file3.read(2))
# print(file3.read(2))
# print(file3.read(2))
file3.close()
