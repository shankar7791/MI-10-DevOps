#Python program to find the sum of sequence of all numbers upto the given number using recursive function

#****Algorithm****
#1.Take a Take a Input of User
#2.Define the function
#3.First check number, numberis less than zero print "Pleas Enter a positive number"
#4.After call a function
#5.Check a number is 1 print 1
#6.Given number is Greater tha 1 performe (n+sum(n-1))and print output
def rsum(n):
   if n <= 1:
       return n
   else:
       return n + rsum(n-1)
n1 = int(input("Enter a Integer Number"))
if n1 < 0:
   print("Pleas Enter a positive number")
else:
   print("The sum is",rsum(n1))


