
import random
month = random.randint(1, 12)

#‰½ŒÌ‚©H‚ª‚È‚¢
if month <= 2:
    print("“~",month)
elif month <= 5:
    print("t",month)
elif month <= 8:
    print("‰Ä",month)
elif month == 12:
    print("“~",month)


#‹Gß‚ğ”»’f‚·‚éŠÖ”‚ğì¬‚·‚é (H‚à’Ç‰Á)
def check_kisetsu(month):
    if month <= 2:
        return("“~")
    elif month <= 5:
        return("t")
    elif month <= 8:
        return("‰Ä")
    elif month <= 11:
        return("H")
    elif month == 12:
        return("“~")
    else:
        return("err")

#ŠÖ”‚Å”»’f‚·‚é
check_kisetsu(1)
check_kisetsu(5)
check_kisetsu(8)
