#Prog 4:  Write a program to check whether a number is divisible by 5 and 11 or not  

num=int(input("Enter the number : "))
if (num%5==0) and (num%11==0) :
    print(f"{num} is divisible by 5 and 11")
else :
     print(f"{num} is not divisible by 5 and 11")

