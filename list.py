tmp_list = []
tmp_list = [4,2,3,1]

#list�ɂ͂Ȃ�ł�����ł���
# (1)������Ɛ��l�����݂��Ă�OK
tmp_list2 = ['a',10,'abc',2.34]

# (2)list�̒���list��������
tmp_list3 = [tmp_list,tmp_list2]
print(tmp_list3)
print(tmp_list3[1][2])#2�ڂ̃��X�g��3�ڂ��Q��

#���p:range�^��list�^�ɕϊ�
tmp_list4 = list(range(1,11))
tmp_list4

#���p:list�̃\�[�g
tmp_list.sort()
print(tmp_list)

#���p:����\�L
tmp=[]
for i in tmp_list2:
    tmp.append(i)
print(tmp)

tmp=[i for i in tmp_list2] #1�s�ł����č���
print(tmp)
