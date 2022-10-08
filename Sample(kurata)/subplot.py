#事前にmatplotlibを環境にinstallすることが必要
import matplotlib.pyplot as plt
import math
import numpy as np

fig = plt.figure()

x=np.arange(-9,10,1)
y=x
ax1 = fig.add_subplot(2,2,1)
ax1.plot(x,y)
ax1.set_title("y=x")

x=np.arange(-9,10,1)
y=x**2 #x^2
ax2 = fig.add_subplot(2,2,2)
ax2.plot(x,y)
ax2.set_title("y=x^2")

x=np.arange(-9,10,1)
y=x**3 #x^3
ax3 = fig.add_subplot(2,2,3)
ax3.plot(x,y)
ax3.set_title("y=x^3")

x=np.arange(-9,10,1)
y=x**4 #x^4
ax4 = fig.add_subplot(2,2,4)
ax4.plot(x,y)
ax4.set_title("y=x^4")
ax4.grid(1)

plt.tight_layout()#図が重ならないようにする

plt.show()
