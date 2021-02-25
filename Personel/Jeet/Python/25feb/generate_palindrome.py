n = int(input('enter any no:'))
while 1:
    temp = str(n)
    temp = int(temp[::-1])
    if n == temp:
        print(f'{n} is palindrome')
        break
    else:
        n +=temp
        
