'''
Write a Python program to construct the following pattern, using a nested while loop.
* 
* * 
* * * 
* * * * 
* * * * * 
* * * * 
* * * 
* * 
*
'''
rows=int(input("Enter the number of rows "))

i=1
while i<= rows:
    j=1
    while j<=i:
        print("*",end=' ')
        j=j+1
    print()
    i=i+1
i=1
while i<=rows:
    j=rows
    while j>i:
        print("*",end=' ')
        j=j-1
    print()
    i=i+1