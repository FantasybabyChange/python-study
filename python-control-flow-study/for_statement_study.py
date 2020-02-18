#for 命令
seq = ['la','he','wa']
# 正常遍历
for w in seq:
    print(w,end="")
print('end')
#range() 遍历数字
for w in range(4):
        print(w)
for w in range(1,4):
    print(w)
chinese_zodiac = '猴鸡狗猪鼠牛虎兔龙蛇马羊'
for i in range(2010,2020):
    print("%s 年是 %s 年"%(i,chinese_zodiac[i%12]))
for i in range(len(chinese_zodiac)):
    print(chinese_zodiac[i])
