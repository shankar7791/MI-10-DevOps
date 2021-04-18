#Pascal's triangle

n = int(input("Enter the rows"))

for i in range(n): 
    # adjust space 
    print(' '*(n-i), end='') 
  
    # compute power of 11 
    print(11**i,' ')