# Program to add two given matrices


x = [[12,7,3], [4 ,5,6], [7 ,8,9]]

y = [[5,8,1], [6,7,3], [4,5,9]]

result = [[0,0,0], [0,0,0], [0,0,0]]

# iterate through rows
for i in range(len(x)):
   # iterate through columns
   for j in range(len(x[0])):
       result[i][j] = x[i][j] + y[i][j]

for r in result:
   print(r)


#2nd program by taking user input and list comprehension


rows = int(input("Enter the Number of rows : " ))
column = int(input("Enter the Number of Columns: "))

print("Enter the elements of First Matrix:")
matrix_a= [[int(input()) for i in range(column)] for i in range(rows)]
print("First Matrix is: ")
for n in matrix_a:
    print(n)

print("Enter the elements of Second Matrix:")
matrix_b= [[int(input()) for i in range(column)] for i in range(rows)]
for n in matrix_b:
    print(n)
    
result=[[0 for i in range(column)] for i in range(rows)]

for i in range(rows):
    for j in range(column):
        result[i][j] = matrix_a[i][j]+matrix_b[i][j]

print("The Sum of Above two Matrices is : ")
for r in result:
    print(r)