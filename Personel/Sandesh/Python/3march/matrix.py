#Python Program to add two matrices using nested for loop.

A = [[5,8,3],
    [4 ,4,6],
    [2 ,3,9]]

B = [[5,9,1],
    [4,5,3],
    [6,5,3]]

result = [[0,0,0],
         [0,0,0],
         [0,0,0]]

for i in range(len(A)):
   for j in range(len(A[0])):
       result[i][j] = A[i][j] + B[i][j]

for r in result:
   print(r)