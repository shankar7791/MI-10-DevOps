n = input('enter string:')
i = len(n)-1
num = '0123456789'
l = 0
d = 0
print(i)
while i>=0:
    if n[i] in num:
        d +=1
    else:
        l +=1
    i -=1
print(f'total letter is:{l}')
print(f'total digit is:{d}')
