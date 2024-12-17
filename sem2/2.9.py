
with open('input.txt', 'r') as file:
    t = file.read()
c = 0
i = 0
while i < len(t):
    if t[i] in '.!?':
        c += 1
        while i < len(t) and t[i] in '.!?':
            i += 1
    else:
        i += 1 

print(c)