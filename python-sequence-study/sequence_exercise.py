#练习题
# 练习一 字符串
# 1. 定义一个字符串Hello Python 并使用print( )输出
# 2. 定义第二个字符串Let‘s go并使用print( )输出
# 3. 定义第三个字符串"The Zen of Python" -- by Tim Peters 并使用print( )输出
str = "Hello Python"
print(str)
str1 = "Let‘s go"
print(str1)
str2 = '''"The Zen of Python" -- by Tim Peters'''
print(str2)

# 练习二 字符串基本操作

# 1. 定义两个字符串分别为 xyz 、abc 
# 2. 对两个字符串进行连接
# 3. 取出xyz字符串的第二个和第三个元素
# 4. 对abc输出10次
# 5. 判断a字符（串）在 xyz 和 abc 两个字符串中是否存在，并进行输出
estr,estr1="xyz","abc"
estr2 = estr + estr1
print(list(estr[1:3]))
print(estr1 * 10)
print(['a' in estr])
print(['a' in estr1])

# 练习三 列表的基本操作
# 1. 定义一个含有5个数字的列表
lists = [1,2,3,4,5]
# 2. 为列表增加一个元素 100
lists.append(100)
# 3. 使用remove()删除一个元素后观察列表的变化
lists.remove(2)
print(lists)
# 4. 使用切片操作分别取出列表的前三个元素，取出列表的最后一个元素
print(lists[0:3])
print(lists[-1])

# 练习四 元组的基本操作

# 1. 定义一个任意元组，对元组使用append() 查看错误信息
tuple1 = tuple((1,2,3,4,5))
# tuple1.append(1)
# 2. 访问元组中的倒数第二个元素
print(tuple1[-2])
# 3. 定义一个新的元组，和 1. 的元组连接成一个新的元组
tuple2 = tuple((6,7,8))
tuple3 = tuple1 + tuple2
print(tuple3)
# 4. 计算元组元素个数
print(len(tuple3))


