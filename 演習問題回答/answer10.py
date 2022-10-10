
import random
month = random.randint(1, 12)

#何故か秋がない
if month <= 2:
    print("冬",month)
elif month <= 5:
    print("春",month)
elif month <= 8:
    print("夏",month)
elif month == 12:
    print("冬",month)


#季節を判断する関数を作成する (秋も追加)
def check_kisetsu(month):
    if month <= 2:
        return("冬")
    elif month <= 5:
        return("春")
    elif month <= 8:
        return("夏")
    elif month <= 11:
        return("秋")
    elif month == 12:
        return("冬")
    else:
        return("err")

#関数で判断する
check_kisetsu(1)
check_kisetsu(5)
check_kisetsu(8)
