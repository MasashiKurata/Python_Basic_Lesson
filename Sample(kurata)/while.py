
i=0
while i<10:
    print(i)
    i = i+1

# break�� 5�܂ŌJ��Ԃ������ꍇ�@slide:101
i=0
while i<10:
    print(i)
    i=i+1
    if i>5:
        break

# continue 5��ڈȍ~�́A"|"���\������Ȃ� slide:103
i=0
while i<10:
    print(i,end=' ')
    i=i+1
    if i>5:
        continue
    print("|",end=' ') #5��ڈȍ~�́A���̍s�����s����Ȃ�

# for. while slide:104
i=0 #�������̏ꍇ�́Abreak�Ŏ~�܂�
#i=10 #�������̏ꍇ�́Abreak�Ŏ~�܂�Ȃ�
while i<10:
    i=i+1
    print(i,end=' ')
    if i>3:
        print("stop by break")
        break;
else:
    print("no break")
