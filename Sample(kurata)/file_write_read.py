﻿# ファイルをopenして文字を書き込む
file = open('mail.txt','w',encoding='utf-8')
file.write("Hello!") #書き込んだ文字数が戻り値
file.close()

#ファイルをopenして文字を読み込む
file=open('mail.txt','r',encoding='utf-8')
file.read()
file.close()

# 作成されたファイルを見るには、ソリューションエクスプローラーの
# Sample(kurata)を選択後、上部のGUIボタン：すべてのファイルを表示する
# を押すこと