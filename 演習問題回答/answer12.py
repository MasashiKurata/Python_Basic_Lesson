
import pandas as pd
data = pd.read_csv(r'Medical_list2.csv',encoding = 'utf-8')
data['BMI'] = round(data['体重'] /((data['身長']/100) ** 2),1)
data.insert(loc = 1, column= ‘性別’, value = 0)  #挿入の場合
data.iloc[0:9,1]='男'
data.iloc[9:,1]='女'
print(data)
