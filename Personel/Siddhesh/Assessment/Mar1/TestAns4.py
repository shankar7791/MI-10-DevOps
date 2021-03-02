# check given string is palindrome or not. *


num =int(input("Enter number:"))
temp=num
rev=0
while(num>0):
    sum=num%10
    rev=rev*10+sum
    num=num//10
if(temp==rev):
    print("The number is a palindrome!")
else:
    print("The number is not a palindrome!")

    