   #Write a Python program to get the factorial of a number using recursion
   
   #****Algorithm****
   #1.Take a Take a Input of User
   #2.Define the function
   #3.If user enter a negative Number than print "Sorry, factorial does not exist for negative numbers"
   #4.Other vice User enter a zero than print "factorial of 0 is 1"
   #5.user enter a integer value than print first  number given by the user, Call function 
   #6.function take a number after check a condition
   #7.if number value one than print one because 1 factorial is 1
   #8.number grather than 1 than go to else block and perfome a
   #9.n*fact(n-1)
   #10.perform and print OutPut
def fact(n):
   if n == 1:
       return n
   else:
       return n*fact(n-1)
n1 = int(input("Enter a Integer number: "))
if n1 < 0:
   print("Sorry, factorial does not exist for negative numbers")
elif n1 == 0:
   print("The factorial of 0 is 1")
else:
   print("The factorial of", n1, "is", fact(n1))

   

   
