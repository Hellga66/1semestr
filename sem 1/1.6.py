with open("input.txt", "r") as infile:
    numbers = infile.readline()
    op = infile.readline()
    base =int( infile.readline())

num = [int(x, base) for x in numbers.split()]

if op == '+':
    res = sum(num)
elif op == '-':
    res = num[0] - sum(num[1:])
elif op == '*':
    res = 1
    for num in numbers:
        res *= num

ans=''

while res > 0:
    ans = str(res % base) + ans
    res //= base


with open("output.txt", "w") as outfile:
    outfile.write(ans)