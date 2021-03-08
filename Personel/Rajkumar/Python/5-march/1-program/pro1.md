#Write a Python program to calculate the sum of a list of numbers using recursion.

#****Algorithm****
#1.Take a Take a Input of User
#2.Define the function
#3.calling A function
#4.go to inside a function and check a If condition 
#5.Condition is true go next line and follow a logic
#6.Logic add a number take a user and (number-1
#7.Will keep repeating and the value of the number does not become zero until print
#8.other vice numbers is less than zero than not show a output
#9.End a program                                                 
def sum(n):                                                      
    if n>0:                                                      
        s=n+sum(n-1)
        print(s,end=", ")
    else:
        s=0
    return s
  
n=int(input("Enter a number"))
sum(n)


