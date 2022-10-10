#-----------------------------------------------------------------
#辞書は "格納されているデータに名前を付けることで扱いを容易にする"
#-----------------------------------------------------------------

#辞書(dict)の作成 'key:value'
adrs = {'yamada': 'tokyo', 'kurata': 'saitama', 'saito': 'gunma'}

#型
print(type(adrs))

#keyの表示
print(adrs.keys())

#valueの表示
print(adrs.values())

#(key,value)の表示
print(adrs.items())

#valueの参照1
print(adrs['yamada'])
print(adrs['kurata'])
print(adrs['saito'])

#valueの参照2
for i in adrs:
    print(i,adrs[i])


#valueの変更
adrs['yamada']='shizuoka'
print(adrs)

#参考：辞書の中に辞書を作成
books = {
    'title1':
    {
        'author': 'かわさき しんじ',
        'contents': 'タプル',
    },
    'title2':
    {
        'author': '一色 政彦',
        'contents': 'Deep Learningコミュニティー……',
    },
    'title3':
    {
        'author': 'かわさき しんじ',
        'contents': 'リストの操作',
    }
}

#辞書の中の辞書の参照
print(books['title2']['author'])

