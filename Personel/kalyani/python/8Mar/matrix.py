# WAP To  find Matrix in z format


R = int(input("Enter the number of rows:")) 
C = int(input("Enter the number of columns:")) 
M1=[]
for i in range(R):         
    a =[] 
    for j in range(C):    
         a.append(int(input())) 
    M1.append(a)

print("First Matrix is for M1:")
for i in range(R): 
    for j in range(C): 
        print(M1[i][j], end = " ") 
    print() 

n = len(M1[0])
print("Matrix in Z format: ")               
i = 0
for j in range(0, n-1):
    print(M1[i][j], end =" ") 
         
k = 1
for i in range(0, n):
    for j in range(n, 0, -1):
        if(j == n-k):
            print(M1[i][j], end = " ") 
            break; 
    k+= 1
 
i = n-1; 
for j in range(0, n):
    print(M1[i][j], end = " ")

   