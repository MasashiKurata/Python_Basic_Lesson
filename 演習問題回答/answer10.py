
import random
month = random.randint(1, 12)

#���̂��H���Ȃ�
if month <= 2:
    print("�~",month)
elif month <= 5:
    print("�t",month)
elif month <= 8:
    print("��",month)
elif month == 12:
    print("�~",month)


#�G�߂𔻒f����֐����쐬���� (�H���ǉ�)
def check_kisetsu(month):
    if month <= 2:
        return("�~")
    elif month <= 5:
        return("�t")
    elif month <= 8:
        return("��")
    elif month <= 11:
        return("�H")
    elif month == 12:
        return("�~")
    else:
        return("err")

#�֐��Ŕ��f����
check_kisetsu(1)
check_kisetsu(5)
check_kisetsu(8)
