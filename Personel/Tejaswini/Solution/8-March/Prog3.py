R = int(input("Enter the number of rows:")) 
C = int(input("Enter the number of columns:")) 

print("Enter the elements of Matrix:")
M1= [[int(input()) for i in range(C)] for i in range(R)]
print("First Matrix is: ")
for n in M1:
    print(n)

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