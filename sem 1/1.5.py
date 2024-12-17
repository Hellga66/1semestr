def f(N, b, c):
    n = int(str(N), b)
    if n == 0:
        return '0'
    s = ''
    while n > 0:
        a = n % c
        s = str(a) + s
        n //= c  

    return s

N, b, c = list(map(int, input().split()))
print(f(N, b, c))