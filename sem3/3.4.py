def print_triangle(size, symb):
    for i in range(1, size + 1):
        print(symb * i)
    for i in range(size - 1, 0, -1):
        print(symb * i)

a=input().split()
print_triangle((int(a[0])+1)//2,a[1])