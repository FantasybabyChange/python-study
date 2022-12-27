import os
file3 = open("txt.txt")
size = os.path.getsize("txt.txt")
inputValue = input("please input:\n")
print(size)
print(inputValue)
print(file3.read(2))
file3.seek(2, 0)
print(file3.tell())
print(file3.read(2))
for line in file3.readlines():
    if line.find(inputValue) >= 0:
        print("yes ")
    else:
        print("不存在")


# print(file3.read(2))
# print(file3.read(2))
file3.close()
