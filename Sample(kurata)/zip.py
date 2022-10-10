fruits=['apple','banana','orange']
prices=[100,198,80]

#2つのリストから一つずつ順番に値を取り出して表示する
for fruit, price in zip(fruits,prices):
    print(fruit,price)
