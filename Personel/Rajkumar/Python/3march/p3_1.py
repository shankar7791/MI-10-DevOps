a = [[1,8,3], [7 ,5,6], [7 ,8,9]]
b = [[6,8,1], [7,7,0], [4,5,]]
c = [[0,0,0], [0,0,0], [0,0,0]]
for i in range(len(a)):
   for j in range(len(a[0])):
       c[i][j] = a[i][j] + b[i][j]
for r in c:
   print(r)