n1 = int(input('Enter first no:'))
n2 = int(input('Enter second no:'))
n3 = int(input('Enter third no:'))

if n1>n2 and n1>n3:
    print(f'{n1} is greatest')
else:
    if n2>n3:
        print(f'{n2} is greatest')
    else:
        print(f'{n3} is greatest')