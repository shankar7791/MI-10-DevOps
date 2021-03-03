# Program 1 : Python Program to add two matrices using nested for loop.

x = [[14,16,18],
    [78,52,10],
    [10,20,30]]

y = [[25,20,10],
    [22,33,44],
    [78,45,45]]

sum = [[0,0,0],[0,0,0],[0,0,0]]

for i in range(len(x)):
   for j in range(len(x[0])):
       sum[i][j] = x[i][j] + y[i][j]

for r in sum:
   print(r)