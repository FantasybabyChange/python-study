# 练习一 函数
# 1. 创建一个函数，用于接收用户输入的数字，并计算用户输入数字的和


def input_function():
    count = 0
    while True:
        result = int(input('please input'))
        if result == -1:
            break
        count += int(result)
        print(count)


# input_function()
# 2. 创建一个函数，传入n个整数，返回其中最大的数和最小的数
def integer_function(*input_num):
    length = len(input_num)
    sorted(input_num, key=lambda x: x)
    return {'big': input_num[length - 1], 'small': input_num[0]}


# print(integer_function(1, 3, 5, 2, 6, 9, 16))
# 3. 创建一个函数，传入一个参数n，返回n的阶乘
def factorial(n):
    result = n
    while n - 1 > 0:
        n -= 1
        result *= n
    print(result)


factorial(5)
