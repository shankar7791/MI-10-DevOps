#Write a Python program to get the factorial of a number using recursion
def fact(number):
    if number==1:
        return 1
    else:
        return number*fact(number-1)

num=int(input("enter the number"))
if num<0:
    print(f"{num} is negitive number")
elif num==0:
    print(f,"{num} factorial of zero is always 1")
else:
    print("fact of number is",fact(num))


#Algoritham
#define a fumction def fact(number)
#check if number ==1
#return 1
#else,retutn number*fact(number-1)
#take input from user
#check if num<0
#then print(number is negitive)
#elif num==0
#print(fact is 1)
#else,goto step 1 and print