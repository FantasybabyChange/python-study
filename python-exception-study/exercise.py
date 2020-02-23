# 练习一 异常
# 1. 在Python程序中，分别使用未定义变量、访问列表不存在的索引、访问字典不存在的关键字观察系统提示的错误信息
# 2. 通过Python程序产生IndexError，并用try捕获异常处理
# print(a)
# b = '123'
# print(b[4])
# c = {'a':'b','b':'d'}
# print(c['c'])
try:
    b = '123'
    print(b[4])
except IndexError as ie:
    print('数组越界')
finally:
    print('finally')