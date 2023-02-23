#from winreg import KEY_ENUMERATE_SUB_KEYS
import pandas as pd
import math
import matplotlib.pyplot as plt
import seaborn as sns

# タイタニック号の乗客員名簿ファイルを読み込む
titanic_data = pd.read_csv(r'titanic.csv')

# データ全体の概要を表示
titanic_data.describe()

# 列名だけ表示
titanic_data.columns

# 行数を表示
titanic_data.count()

# 死亡者数、生存者数の表示
titanic_data[titanic_data['Survived']==0]['Survived'].count()
titanic_data[titanic_data['Survived']==1]['Survived'].count()

t=titanic_data
t[t['Survived']==1]['Fare'].mean()
t[t['Survived']==0]['Fare'].mean()

# 列項目の内容
# PassengerId – 乗客識別ユニークID
# Survived – 生存フラグ（0=死亡、1=生存）
# Pclass – チケットクラス
# Name – 乗客の名前
# Sex – 性別（male=男性、female＝女性）
# Age – 年齢
# SibSp – タイタニックに同乗している兄弟/配偶者の数
# parch – タイタニックに同乗している親/子供の数
# ticket – チケット番号
# Fare – 料金
# cabin – 客室番号
# Embarked – 出港地（タイタニックへ乗った港）

#亡くなった人の男女比
t.pivot_table(index="Sex",columns="Survived",aggfunc="size",fill_value=0)

# 年齢層
plt.hist(t["Age"])
plt.show()

# 支払料金分布
plt.hist(t["Fare"])
plt.show()

# クラスタリング
# (1)データを限定する
columns = ["Survived","Pclass","Sex","Age","Fare"]
t = t[columns]
# (2)欠損値を処理する
t.isnull().sum()

mean_ = t['Age'].mean()
t['Age'] = t['Age'].fillna(mean_)

mean_ = t['Fare'].mean()
t['Fare'] = t['Fare'].fillna(mean_)

# (3) ダミー変数処理(文字列->数値)
t = pd.get_dummies(t,drop_first=True)

# (4) データを標準化する
from sklearn.preprocessing import StandardScaler

sc = StandardScaler()

df_sc = sc.fit_transform(t)
df_sc = pd.DataFrame(df_sc, columns=t.columns)

from sklearn.cluster import KMeans
model = KMeans(n_clusters=4, random_state=1)
model.fit(df_sc)

cluster = model.labels_
t['clusters'] = cluster

t.groupby('clusters').mean()

# 以下のグループに分類できた
#cluster0: 平均42歳、高い料金、男、生存率17%
#cluster1: 平均26歳、低い料金、男、生存率0
#cluster2: 平均24歳、低い料金、女、生存率80%
#cluster3: 平均36歳、高い料金、女、生存率92%

fig, axes = plt.subplots(2,3,figsize=(14,6))
sns.barplot(ax=axes[0,0], data=t, x='clusters', y='Survived')
sns.barplot(ax=axes[0,1], data=t, x='clusters', y='Pclass')
sns.barplot(ax=axes[0,2], data=t, x='clusters', y='Age')
sns.barplot(ax=axes[1,0], data=t, x='clusters', y='Fare')
sns.barplot(ax=axes[1,1], data=t, x='clusters', y='Sex_male')
plt.show()

