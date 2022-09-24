import pandas as pd

#data frameにcsvファイルを読み込む
data = pd.read_csv(r"C:\Users\user\Desktop\Medical_List.csv",encoding='utf-8')

print(data)
