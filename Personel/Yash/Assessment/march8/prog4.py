# Program 4 : Write a function which implements the Pascal's triangle using recursive function

from math import factorial 
n = int(input("Enter the no of rows : "))
for i in range(n): 
    for j in range(n-i+1): 
        print(end=" ")   
    for j in range(i+1): 
        print(factorial(i)//(factorial(j)*factorial(i-j)), end=" ") 
    print() 