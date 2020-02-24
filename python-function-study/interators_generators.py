# 迭代器和生成器
# str = 'abv'
# interStr = iter(str)
# print(next(interStr))
# print(next(interStr))
# print(next(interStr))
# print(next(interStr))
#generators
def  rangf(start,end,step):
        while start < end:
            yield start
            start += step

for v in rangf(1,20,1.5):
    print(v)



