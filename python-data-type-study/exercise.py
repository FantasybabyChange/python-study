# 练习一 字典的使用

# 1. 定义一个字典，分别使用a、b、c、d作为字典的关键字，值为任意内容
# 2. 为该字典增加一个元素‘c':'cake'后，将字典输出到屏幕
# 3. 取出字典中关键字为d的值
dirc1 = {"a":"1","b":"2"}
dirc1['c'] = "3"
print(dirc1)
print(dirc1['b'])

# 练习二 集合的使用
# 1. 将字符串hello中每个字符赋值给一个集合，将这个集合输出到屏幕
str='hello'
cstr = []
for i in range(len(str)):
    cstr.append(str[i])
print(cstr) 