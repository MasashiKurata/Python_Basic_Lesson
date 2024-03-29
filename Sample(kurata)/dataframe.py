﻿import pandas as pd
import math

#リストから作る
list1=["a1","a2","a3"]
print(pd.DataFrame(data=list1))

#直接作る
df = pd.DataFrame(['a1','a2','a3'])

#辞書で作る
d = {"0":['a1', 'a2', 'a3']}
df2 = pd.DataFrame(d)

#ファイルから読み込む (1)
data = pd.read_csv(r"Medical_List.csv",encoding='utf-8')
data['名前']
data[['身長','体重']]
data['身長'].sum()
data['身長'].mean()
data.describe()

# loc,iloc
# locを利用するとDataFrameからインデックス、列名を指定してデータを抽出でき、スライシングを使うことが可能。
data.loc[0:10,"名前"]

# ilocを利用するとDataFrameから行・列番号を指定してデータを抽出でき、スライシングを使うことが可能。
data.iloc[2:5,0:3]

# 170cm以上の人の名前　slide 146
data[data['身長']>170]['名前']

# 列の追加 slide 148
data['性別']=0

# inplace  slide 154
data_tmp = data.drop(index=1,inplace=False) #もとのデータを変更しない
#dataとdata_tmpを比較する




