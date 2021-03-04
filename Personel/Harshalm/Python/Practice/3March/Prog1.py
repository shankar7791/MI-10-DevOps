#Python Program to add two matrices using nested for loop.


X = [[11, 9, 5],
    [6, 4, 8],
    [7, 2, 1]]


Y = [[8, 1, 6],
    [11, 3, 4],
    [9, 2, 3]]  

Z = [[0, 0, 0],
    [0, 0, 0],
    [0, 0, 0]]

for i in range(len(X)) :    #iterate from rows
    for j in range(len(X[0])) :  #iterate from column
        Z[i][j] = X[i][j] + Y[i][j]

for k in Z :
    print(k)



