#Python Program for Program to Print Matrix in Z form 

rows = int(input("Enter the Number of rows : " ))
column = int(input("Enter the Number of Columns: "))

print("Enter the elements of Matrix:")
matrix_a= [[int(input()) for i in range(column)] for i in range(rows)]
print("First Matrix is: ")
for n in matrix_a:
    print(n)

a = len(matrix_a[0])
                  
i = 0
for j in range(0, a-1):
    print(matrix_a[i][j], end = ' ') 
         
k = 1
for i in range(0, a):
    for j in range(a, 0, -1):
        if(j == a-k):
            print(matrix_a[i][j], end = ' ') 
            break; 
    k+= 1
 
# Print last row
i = a-1; 
for j in range(0, a):
    print(matrix_a[i][j], end = ' ')