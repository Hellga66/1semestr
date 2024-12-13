import numpy as np
def spiral(n,m):
    A=np.zeros((n,m))
    a,i,j=1,0,0
    while(a<m*n):
        while(j+1<m and A[i][j+1]==0):
            A[i][j]=a 
            a+=1
            j+=1
        while(i+1<n and A[i+1][j]==0):
            A[i][j]=a 
            a+=1
            i+=1
        while(j>0 and A[i][j-1]==0):
            A[i][j]=a 
            a+=1
            j-=1
        while(j+1<m and A[i-1][j]==0):
            A[i][j]=a 
            a+=1
            i-=1
    A[i][j]=a
    return A
print (spiral(7,8))