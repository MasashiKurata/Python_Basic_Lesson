
import pandas as pd
import matplotlib.pyplot as plt
plt.rcParams['font.family'] = "MS Gothic"

data = pd.read_csv(r'Medical_list2.csv',encoding = 'utf-8')
#print(data)
data['BMI'] = round(data['体重'] /((data['身長']/100) ** 2),1)
data.insert(loc = 1, column= '性別', value = 0)  #挿入の場合
data.iloc[0:9,1]='男'
data.iloc[9:,1]='女'
#data

data1 = data

#fig, ex1 = plt.subplots(1,1,figsize=(6,4))  #グラフサイズ
fig = plt.figure(figsize=(12,4))

ex1 = fig.add_subplot(1,2,1)
ex2 = ex1.twinx()

colors=[('plum' if i == '女' else 'skyblue') for i in data.性別]


ex1.bar(data.index, data['BMI'], color=colors,tick_label=data.index.values)
ex2.plot(data.index, data['身長'], color='yellow',marker=".",label='身長')

plt.title('BMIと身長',loc='center')

ex1.set_ylim(0,40)
ex2.set_ylim(150,180)
handler1, label1 = ex1.get_legend_handles_labels()    #凡例表示準備
handler2, label2 = ex2.get_legend_handles_labels()    #凡例表示準備
ex1.legend(handler1+handler2,label1+label2,borderaxespad=0)  #凡例表示
#plt.savefig('BMIと身長.png')
#plt.show()
plt.grid()


#fig, ex1 = plt.subplots(1,1,figsize=(6,4))
ex1 = fig.add_subplot(1,2,2)
ex2 = ex1.twinx()

#ex1.bar(data1.index, data1['BMI'], color=colors,tick_label=data.名前)
ex1.bar(data1.index, data1['BMI'], color=colors,tick_label=data.index.values)
ex2.plot(data1.index, data1['体重'], color='yellow',marker=".",label='体重')
plt.title('BMIと体重',loc='center')

ex1.set_ylim(0,40)
ex2.set_ylim(45,100)
handler1, label1 = ex1.get_legend_handles_labels()
handler2, label2 = ex2.get_legend_handles_labels()
ex1.legend(handler1+handler2,label1+label2,borderaxespad=0)
#plt.savefig('BMIと体重.png')
#fig.show()
plt.grid()
plt.show()
