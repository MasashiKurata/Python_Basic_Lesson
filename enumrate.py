#for i in range(2,110,2):
#    print(i,end=',')

#numを見れば何回for文が回っているか確認できる
for num,i in enumerate(range(2,110,2)):
    print(num,i)

#以下でも同じ(C言語風)
num=0
for i in range(2,110,2):
    print(num,i)
    num +=1

# 参考:C言語の場合
#
##include <stdio.h>
#int num=0
#for (int i=0;i<110;i=i+2) {
#    printf("%d %d\n",num,i);
#    num++;    
#}

#参考:辞書からの値取り出し
kakaku={'apple':100,'banana':110,'orange':150}
for (fruit,price) in enumerate(kakaku.items()):
    print(fruit,price)
