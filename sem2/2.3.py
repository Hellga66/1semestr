def p(s):
    return s==s[::-1]

def m(s):
    dict={'A':'A','H':'H','I':'I','M':'M','O':'O', 
          'T':'T','U':'U','V':'V','W':'W','X':'X',
          'Y':'Y','1':'1','8':'8','E':'3','3':'E',
          'J':'L','L':'J','S':'2','2':'S','Z':'5','5':'Z'}
    a=[]
    for i in s:
        if i in dict:
            a.append(dict[i])
        else:
            return False
    return True

x=input()
if p(x) and m(x):
    print(f'{x}  is a mirrored palindrome.')
elif p(x):
    print(f'{x} is a regular palindrome.')
elif m(x):
    print(f'{x} is a mirrored string.')
else:
    print(f'{x}  is not a palindrome')