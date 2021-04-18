#count prime no within range
n = int(input('enter a number where you want the prime no.s:'))
count = 0
for i in range(2,n+1):
    for j in range(2,i):
        if i%j == 0:
            break
    else:
        count +=1
print(f'total prime no.s upto {n} is equal to: {count}')
