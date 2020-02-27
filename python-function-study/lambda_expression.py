# lambda expression
def anon_function(n):
    return lambda a, b: a + b + n


f1 = anon_function(3)
print(f1(1, 2))  # 6
# sorted(nameWithCount.items(), key=lambda item: item[1], reverse=True)
# lambda item: item[1]  =>

# def f1(item):
#     return item[1]
