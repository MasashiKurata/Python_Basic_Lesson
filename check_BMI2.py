import pandas as pd
import matplotlib.pyplot as plt
import check_BMI #他のソースから関数を呼ぶ

# import check_BMIしない場合
#def check(bmi):
#    if  bmi<18.5:
#        return('低体重')
#    elif 18.5 <= bmi < 25:
#        return('普通体重')
#    elif 25 <= bmi < 30:
#        return('肥満:1度')
#    elif 30 <= bmi < 35:
#        return('肥満:2度')
#    elif 35 <= bmi < 40:
#        return('肥満:3度')
#    else:
#        return('肥満:4度')

# for debug
#print(check_BMI.check(100))

data = pd.read_csv(r"C:\Users\user\Desktop\Medical_List2.csv",encoding='utf-8')
bmi = round(data['体重']/((data['身長']/100)**2),1)

# 方法1 (1行毎に判定して値を変更)
#data['判定'] = ""
#for num,i in enumerate(bmi):
#    data.loc[num,'判定'] = check_BMI.check(i)
#print(data)

# 方法2 (1度に判定して値を変更)
data['判定'] = ""
data['判定'] = bmi.apply(check_BMI.check)#全部の行に関数を適用して結果を取得する
print(data)

data['BMI']=bmi
#plt.bar(data['名前'],data['BMI'])
#plt.show()

# 相関を確認する
#data.corr()

#0～0.3未満：ほぼ無関係
#0.3～0.5未満：非常に弱い相関
#0.5～0.7未満：相関がある
#0.7～0.9未満：強い相関
#0.9以上：非常に強い相関

# グラフ表示
#plt.plot(data.index,data['BMI'])
#plt.show()
