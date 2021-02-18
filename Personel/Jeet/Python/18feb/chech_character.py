c = input('Enter any character:')
alphabet = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
special = '`~!@#$%^&*()-_=+[|]{;}:,<.>/?\\\'\"'
if c in alphabet:
    print(f'{c} is alphabet')
elif c in special:
    print(f'{c} is Special character')
else:
    print(f'{c} is number')