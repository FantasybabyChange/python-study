#if 控制 
chinese_zodiac = '猴鸡狗猪鼠牛虎兔龙蛇马羊'
inputValue  =  input()
currentZodiac = chinese_zodiac[int(inputValue) % 12]
if currentZodiac == '鼠':
    print('鼠年大吉吧')
elif currentZodiac == '猪':
    print('猪年大吉吧')
else:
    print('大吉吧')
