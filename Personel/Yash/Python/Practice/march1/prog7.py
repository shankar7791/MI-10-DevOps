rows = int(input("Enter the rows : "))  
for i in range(0,rows):    
    for j in range(0,i+1):  
        print("*",end = "")  
    print() 

for i in range(1,rows+1):    
    for j in range(1,i+1):  
        print(i,end = "")  
    print()

for i in range(1,rows+1):    
    for j in range(1,i+1):  
        print(j,end = "")  
    print()  
   