n = int(input('enter range:'))
o = 0
e = 0
while n>0:
    if n%2 == 0:
        o +=1
    else:
        e +=1
    n -=1
print(f'total odd numbers are {o}')
print(f'total even numbers are {e}')