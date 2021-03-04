#Python Program to add two matrices using nested for loop
X = [[10,17,3],
    [4 ,25,16],
    [17 ,8,19]]

Y = [[15,8,10],
    [16,27,63],
    [14,25,39]]

result = [[0,0,0],
         [0,0,0],
         [0,0,0]]

for i in range(len(X)):
   for j in range(len(X[0])):
       result[i][j] = X[i][j] + Y[i][j]

for r in result:
   print(r)