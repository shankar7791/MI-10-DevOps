#Write a Python program to create the multiplication table of a number.

n = int(input("Input a number: "))


for i in range(1,11):       # use for loop to iterate 10 times
   print(n,'x',i,'=',n*i) 
