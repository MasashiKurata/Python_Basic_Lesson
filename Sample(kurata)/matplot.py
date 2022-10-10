#事前にmatplotlibを環境にinstallすることが必要
import matplotlib.pyplot as plt
import math
import numpy as np

#y=x^2のグラフ
x=[-9,-8,-7,-6,-5,-4,-3,-2,-1,0,1,2,3,4,5,6,7,8,9]
y=[81,64,49,36,25,16,9,4,1,0,1,4,9,16,25,36,49,64,81]
plt.plot(x,y)
plt.grid(1)
plt.show()

#参考:同じことをもっと簡単に
x=[]
y=[]
x=np.arange(-9,10,1)
y=x**2 #x^2
plt.plot(x,y)
plt.grid(1)
plt.show()

