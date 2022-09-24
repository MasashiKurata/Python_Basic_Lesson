import pandas as pd
import math

#リストから作る
list1=["a1","a2","a3"]
print(pd.DataFrame(data=list1))

#直接作る
df = pd.DataFrame(['a1','a2','a3'])

#辞書で作る
d = {"0":['a1', 'a2', 'a3']}
df2 = pd.DataFrame(d)


