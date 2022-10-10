
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

plt.rcParams['font.family'] = "MS Gothic"

data = pd.read_csv(r'Medical_list2.csv',encoding = 'utf-8')
#print(data)
data['BMI'] = round(data['体重'] /((data['身長']/100) ** 2),1)
data.insert(loc = 1, column= '性別', value = 0)  #挿入の場合
data.iloc[0:9,1]='1'
data.iloc[9:,1]='0'
data.drop('名前',axis=1)
data.drop('NO',axis=1)
corr = data.corr()

sns.heatmap(corr, cmap='coolwarm', vmin=-1, vmax=1, annot=True)
plt.show()
#ここにBreakPointを設定する