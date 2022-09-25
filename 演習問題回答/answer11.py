
import pandas as pd
data = pd.read_csv(r'Medical_list2.csv',encoding = 'utf-8')
data['BMI'] = round(data['体重'] /((data['身長']/100) ** 2),1)
print(data)