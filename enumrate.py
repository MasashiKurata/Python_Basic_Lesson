#for i in range(2,110,2):
#    print(i,end=',')

#num������Ή���for��������Ă��邩�m�F�ł���
for num,i in enumerate(range(2,110,2)):
    print(num,i)

#�ȉ��ł�����(C���ꕗ)
num=0
for i in range(2,110,2):
    print(num,i)
    num +=1

# �Q�l:C����̏ꍇ
#
##include <stdio.h>
#int num=0
#for (int i=0;i<110;i=i+2) {
#    printf("%d %d\n",num,i);
#    num++;    
#}

#�Q�l:��������̒l���o��
kakaku={'apple':100,'banana':110,'orange':150}
for (fruit,price) in enumerate(kakaku.items()):
    print(fruit,price)
