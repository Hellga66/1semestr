import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
fig = plt.figure(figsize = (16,9)) # создали рисунок/Figure Fig пропорциями 16:9
ax1 = fig.add_subplot(211) # создали Axes (подграфик) ax1 в серии из 2 графиков, поставили на позицию [1,1] -- левый верхний угол
ax2 = fig.add_subplot(212)
df = pd.read_csv('iris_data.csv')
a=list(df['Species'])
l1=[(a.count('Iris-setosa'))/len(a),(a.count('Iris-versicolor'))/len(a),(a.count('Iris-virginica'))/len(a)]
ax1.pie(l1, labels = ['Iris-setosa','Iris-versicolor','Iris-virginica'])
ax1.set_title('Iris species')
b=list(df['PetalLengthCm'])
b1=[]
for i in range(len(b)):
    if i<1.2:
        b1.append(0)
    elif i>1.2 and i<1.5:
        b1.append(1)
    else:
        b1.append(2)
l2=[(b1.count(0))/len(b),(b1.count(1))/len(b),(b1.count(2))/len(b)]
ax2.pie(l2, labels = ['<1.2','1.2<1.5','>1.5'])
ax2.set_title('PetalLengthCm')
plt.show()