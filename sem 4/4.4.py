import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
# fig = plt.figure(figsize = (16,9)) # создали рисунок/Figure Fig пропорциями 16:9
df = pd.read_csv('iris_data.csv')
a1=list(df['SepalLengthCm'])
a2=list(df['SepalWidthCm'])
a3=list(df['PetalLengthCm'])
a4=list(df['PetalWidthCm'])
# plt.figure(figsize=(8,5), dpi=100)

# Line 1

# Основные возможные аргументы функции plot. По умолчанию необходимы только x и y
#plt.plot(x,y, label='2x', color='red', linewidth=2, marker='.', linestyle='--', markersize=10, markeredgecolor='blue')

#нарисуем график первой функции -- 2x
plt.plot(a1,a2, 'b^-')
plt.plot(a1,a3, 'r^-')
plt.plot(a1,a4,'g^-')
plt.plot(a2,a3,color=[0.1,0.7,0.2],marker='.')
plt.plot(a2,a4,color=[0.8,0.7,0.2],marker='.')

plt.plot(a3,a4,color=[0.7,0.1,0.7],marker='.')


def MNK(x,y):
    x=np.array(x)
    y=np.array(y)
    a=((x*y).mean()-x.mean()*y.mean())/((x**2).mean()-x.mean()**2)
    b=y.mean()-a*x.mean()
    return a,b

x = np.array([0,12]) # две точки аппроксимирующей прямой

plt.plot(x, MNK(a3,a4)[0]*x+MNK(a3,a4)[1],"-",color=[0.7,0,0.7],linewidth=3)
plt.plot(x, MNK(a1,a4)[0]*x+MNK(a1,a4)[1],"g-",linewidth=3)
plt.xlabel('X Axis')
plt.ylabel('Y Axis')

plt.grid()
plt.legend()
plt.show()