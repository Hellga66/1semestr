with open('input.txt', 'r') as file:
    num = list(map(float, file.readline().split()))
    op = file.readline()

res = 0
if op == '+':
    result = sum(num) 
elif op == '-':
    res = num[0]    
    for i in num[1:]:  
        res -= i
elif op == '*':
    res = 1
    for i in num:      
        res *= i

with open('output.txt', 'w') as file:
    file.write(str(result)) 