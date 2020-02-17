#通过 年份判断出是什么生肖
chinese_zodiac = '猴鸡狗猪鼠牛虎兔龙蛇马羊'

print(chinese_zodiac[0])
print(chinese_zodiac[-2])
print(chinese_zodiac[0:4])
print(len(chinese_zodiac))

#+
a = 'ab'
b = 'cd'
print(a+b)
#in ,not in
print(['ha' in chinese_zodiac])
print(['ha' not in chinese_zodiac])
# *
print('ha' * 3 )
print(list(filter(lambda x: x =='鸡', chinese_zodiac)))
