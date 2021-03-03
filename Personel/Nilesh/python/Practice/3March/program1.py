#Python Program to add two matrices using nested for loop.
a = [[1,2,3],
    [2,1,3],
    [3,2,1]]

b = [[4,5,6],
    [5,4,6],
    [6,5,4]]

result = [[0,0,0],
         [0,0,0],
         [0,0,0]]

for i in range(len(a)):
    for j in range(len(a[0])):
        result[i][j] = a[i][j] + b[i][j]
for r in result:
    print(r)