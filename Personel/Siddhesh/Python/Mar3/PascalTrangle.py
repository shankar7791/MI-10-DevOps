#Python program to print Pascal's Triangle


n =int(input("Enter the Number: "))

for i in range(n): 
    # adjust space 
    print(' '*(n-i), end='') 
  
    # compute power of 11 
    print(' '.join(map(str, str(11**i)))) 

