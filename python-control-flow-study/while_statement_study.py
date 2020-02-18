#while 命令
a = 0
while a < 100:
    if a<20:
        print('%s 比较小' %(a))
        a += 1
        continue
    if a == 30:
        print('%s 结束了 '% (a))
        break
    a+=1
