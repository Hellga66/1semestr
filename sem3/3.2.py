from math import sqrt,ceil
def prime_fac(n):  
    for i in range(2, ceil(sqrt(n))):
        while n % i == 0: 
            print(i) 
            n = n / i 
    if n > 1: 
        print(n) 
 
n = 200 
prime_fac(n) 
