#通过 年份判断出是什么生肖
chinese_zodiac = '猴鸡狗猪鼠牛虎兔龙蛇马羊'
#年
year = 2020

print(chinese_zodiac[year % 12])
