# Program 3 : Write a Python program to reverse the digits of a given number and add it to the original, If the sum is not a palindrome repeat this procedure.


n = int(input('enter any no:'))
while 1:
    temp = str(n)
    temp = int(temp[::-1])
    if n == temp:
        print(f'{n} is palindrome')
        break
    else:
        n += temp
