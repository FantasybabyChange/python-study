#映射类型-字典
dict1 = {}
print(type(dict1)) #dict

zodiac_name = (u'摩羯座', u'水瓶座', u'双鱼座', u'白羊座', u'金牛座', u'双子座',
               u'巨蟹座', u'狮子座', u'处女座', u'天秤座', u'天蝎座', u'射手座')

zodiac_days = ((1, 20), (2, 19), (3, 21), (4, 21), (5, 21), (6, 22),
               (7, 23), (8, 23), (9, 23), (10, 23), (11, 23), (12, 23))
chinese_zodiac = '猴鸡狗猪鼠牛虎兔龙蛇马羊'
#统计输入过的生肖
# cCount = {}
# for cz in chinese_zodiac:
#     cCount[cz] =0
#通过推导式
cCount = {cz:0 for cz in chinese_zodiac}
#统计输入过的星座
# zCount = {}
# for zn in zodiac_name:
#     zCount[zn] = 0
zCount = {zn: 0 for zn in zodiac_name}
def printCountData():
    for c in cCount:
        print("%s出现了%d" % (c, cCount[c]))
    for z in zCount:
        print("%s出现了%d" % (z, zCount[z]))
def printCurrentZodiac(year,month,day):
    # print("%s 年是 %s 年" % (year, chinese_zodiac[year % 12]))
    cCount[chinese_zodiac[year % 12]] += 1
    count = 0
    while zodiac_days[count] < (month, day):
        if month >= 12 and day > 23:
            break
        count += 1
    # print(zodiac_name[count])
    zCount[zodiac_name[count]] += 1

while True:
    year = int(input('input the year:'))
    month = int(input('input the month:'))
    day = int(input('input the day:'))

    #主体
    printCurrentZodiac(year,month,day)
    printCountData()

