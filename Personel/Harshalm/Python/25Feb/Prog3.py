# Write a Python program to reverse the digits of a given number and add it to the original, If the sum is not a palindrome repeat this procedure. 

num = int(input("Enter a number :-"))

temp = num
rev = 0
while num > 0 :
    sum = num % 10
    rev = rev * 10 + sum
    num = num // 10

if temp == rev :
    print("The number is Palindrome ")
else :
    print("The number is not a palindrome")


