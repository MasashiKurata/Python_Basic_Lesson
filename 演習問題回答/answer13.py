
import pandas as pd
data = pd.read_csv(r'Medical_list2.csv',encoding = 'utf-8')
data['BMI'] = round(data['体重'] /((data['身長']/100) ** 2),1)
data.insert(loc = 1, column= '性別', value = 0)
data.iloc[0:9,1]='男'
data.iloc[9:,1]='女'

def BMI_Class(bmi):
   if  bmi < 18.5:
        return('低体重')
   elif 18.5 <= bmi < 25:
        return('普通体重')
   elif 25 <= bmi < 30:
        return('肥満:1度')
   elif 30 <= bmi < 35:
        return('肥満:2度')
   elif 35 <= bmi < 40:
        return('肥満:3度')
   else:
        return('肥満:4度')

data['BMI判定']=data['BMI'].apply(BMI_Class)
print(data)
