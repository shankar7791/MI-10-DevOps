n = int(input('Enter no:'))

#1.If statement
if n > 0:
    print(f'{n} is positive')

#2.If else statement
if n % 2 == 0:
    print(f'{n} is even')
else:
    print(f'{n} is odd')

#3.If else nested
if n < 50:
    if n > 25:
        print(f'{n} is greater than 25')
    else:
        print(f'{n} is less than 25')
else:
    if n > 75:
        print(f'{n} is greater than 75')
    else:
        print(f'{n} is greater than 50 and less than 75')

#4.If else ladder
if n > 100:
    print(f'{n} is greater than 100')
elif n >75:
    print(f'{n} is between 75 and 100')
elif n>50:
    print(f'{n} is between 50 and 75')
else:
    print(f'{n} is less than 50')

#5.Short-hand If
if n > 0: print(f'{n} is positive')

#6.Short-hand If else
print(f'{n} is even') if n%2==0 else print(f'{n} is odd')