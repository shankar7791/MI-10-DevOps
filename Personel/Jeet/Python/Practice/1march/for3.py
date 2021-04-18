#triangle pattern
n = int(input('enter no of rows:'))
k = n-1
for i in range(n):
    for j in range(k):
        print(end=' ')
    k -=1
    
    for j in range(i+1):
        print('*', end=' ')
    
    print()