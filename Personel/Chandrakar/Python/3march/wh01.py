#Python Program to add two matrices using nested for loop
mat1 = [[10,20,30],
      [40,50,60],
      [70,80,90]]
mat2 = [[90,80,70],
      [60,50,40],
      [30,20,10]]
sum = [[0,0,0],
       [0,0,0],
       [0,0,0]]
for x in range(len(mat1)):
    for y in range(len(mat1[0])):
        sum[x][y] = mat1[x][y]+mat2[x][y]
for z in sum:
    print(z)             
                   