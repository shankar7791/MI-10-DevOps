#Write a Python program to print alphabet pattern 'A'.
n = int(input('enter the size:'))
j = int(n//2)
print(end=' ')
print(f'*'* j)
for i in range(j-1):
    print('*', end='')
    print(' '* j, end='')
    print('*')
print('*'* (j+2))
for i in range(j):
    print('*', end='')
    print(' '* j, end='')
    print('*')
