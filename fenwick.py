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






  