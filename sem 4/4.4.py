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

plt.xlabel('X Axis')
plt.ylabel('Y Axis')

plt.grid()
plt.legend()
plt.show()