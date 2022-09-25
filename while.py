
i=0
while i<10:
    print(i)
    i = i+1

# break文 5まで繰り返したい場合　slide:101
i=0
while i<10:
    print(i)
    i=i+1
    if i>5:
        break

# continue 5回目以降は、"|"が表示されない slide:103
i=0
while i<10:
    print(i,end=' ')
    i=i+1
    if i>5:
        continue
    print("|",end=' ') #5回目以降は、この行が実行されない

# for. while slide:104
i=0 #こっちの場合は、breakで止まる
#i=10 #こっちの場合は、breakで止まらない
while i<10:
    i=i+1
    print(i,end=' ')
    if i>3:
        print("stop by break")
        break;
else:
    print("no break")
