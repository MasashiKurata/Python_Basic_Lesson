# slide 46
menu = ['soup','rice','cake']
menu

#---- list参考 ----

tmp_list = []
tmp_list = [4,2,3,1]


#listにはなんでも代入できる
# (1)文字列と数値が混在してもOK
tmp_list2 = ['a',10,'abc',2.34]

# (2)listの中にlistを代入する
tmp_list3 = [tmp_list,tmp_list2]
print(tmp_list3)
print(tmp_list3[1][2])#2つ目のリストの3つ目を参照

#応用:range型をlist型に変換
tmp_list4 = list(range(1,11))
tmp_list4

#応用:listのソート
tmp_list.sort()
print(tmp_list)

#応用:内包表記
tmp=[]
for i in tmp_list2:
    tmp.append(i)
print(tmp)

tmp=[i for i in tmp_list2] #1行でかけて高速
print(tmp)
