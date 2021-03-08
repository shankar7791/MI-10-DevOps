#Write a Python program to calculate the sum of a list of numbers using recursion.
"""
Alogorithm

1. define function and it's parameter 
2. take variable for the storing the sum of list 
3. Define the for condition for function
3. use recursive method in for loop
4. return function 
5. print statement 
"""

def listsum(numList):
    theSum = 0
    for i in numList:
        theSum = theSum + i
    return theSum

print(listsum([5,4,8,7,10]))

