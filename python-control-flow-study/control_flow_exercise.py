# 练习一 条件语句的使用
# 1. 使用if语句判断字符串的长度是否等于10，根据判断结果进行不同的输出
str = 'agbasda'
if len(str) > 10:
    print('big than 10')
else:
    print('small than 10')
# 2. 提示用户输入一个1-40之间的数字，使用if语句根据输入数字的大小进行判断，如果输入的数字在 1-10，11-20，21-30，31-40，分别进行不同的输出
inputValue = int(input('input 1-40:'))
valueScope = ((1, 10), (11, 20), (21,30),(31, 40))
n = 0
while n < len(valueScope):
    if inputValue >= valueScope[n][0] and inputValue <= valueScope[n][1]:
        print(valueScope[n])
        break
    n += 1
# 练习二 循环语句的使用
# 1. 使用for语句输出1-100之间的所有偶数
for i in range(1,101):
    if i % 2 == 0:
        print('%s 是偶数' % (i))
# 2. 使用while语句输出1-100之间能够被3整除的数字
i = 1
while i  < 101:
    if i % 3 == 0:
        print('%s 能被3整除' %(i))
    i += 1
