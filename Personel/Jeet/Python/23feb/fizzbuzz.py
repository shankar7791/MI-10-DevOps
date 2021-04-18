n =1
while n<=50:
    if n%3 == 0 and n%5 == 0:
        print(f'{n}:FizzBuzz')
    elif n%3 == 0:
        print(f'{n}:Fizz')
    elif n%5 == 0:
        print(f'{n}:Buzz')
    else:
        pass
    n +=1