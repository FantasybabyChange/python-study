#List comprehensions 列表推导式
zCount = []
for zn in range(11):
    if zn%2 == 0:
        zCount.append(zn**2)
print(zCount)

squares = list(map(lambda x: x**2, range(11)))
print(squares)
#使用推导式
zCount = [zn**2 for zn in range(11) if zn%2==0]
print(zCount)
