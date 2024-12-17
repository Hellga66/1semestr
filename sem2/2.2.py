g, s = input().split()
g = int(g)
s = list(s)

result = []
for i in range(0, len(s), g):
    result += s[i:i+g][::-1]

print(''.join(result))