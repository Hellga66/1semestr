class FenwickTree:
    def __init__(self, size):
        self.size = size
        self.tree = [0] * (size + 1) 

    def update(self, i, delta):
        while i <= self.size:
            self.tree[i] += delta
            i += i & -i  

    def sum(self, i):
        sum = 0
        while i > 0:
            sum += self.tree[i]
            i -= i & -i  
        return sum

    def range_sum(self, start, end):
        return self.sum(end) - self.sum(start - 1)



n=int(input())
while n>0:
    m=int(input())
    num=[0]+list(int(x) for x in input().split())
    ft=FenwickTree(m)
    for i in range (1,m+1):
        if num[i]>ft.tree[i-1]:
            ft.update(i,num[i])
        else:
            break

    n-=1
    print(ft.range_sum(1,m))


  