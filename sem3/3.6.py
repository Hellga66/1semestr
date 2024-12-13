import numpy as np
def MNK(x,y):
    x=np.array(x)
    y=np.array(y)
    a=((x*y).mean()-x.mean()*y.mean())/((x**2).mean()-x.mean()**2)
    b=y.mean()-a*x.mean()
    return a,b
x=[1,2,3,4,5,6,7,8,9,10]
y=[10,9,8,7,6,5,4,3,2,1]
print(MNK(x,y))