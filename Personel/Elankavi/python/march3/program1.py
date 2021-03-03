#program to add two matrices using nested for loop
a=[[1,3,3],
   [4,5,6],
   [7,8,9]]
b=[[9,8,7],
   [6,6,4],
   [3,2,2]]

result=[[0,0,0],
        [0,0,0],
        [0,0,0]]
for i in range(len(a)):
    for j in range(len(a[0])):
        
        result[i][j]=a[i][j]+b[i][j]

print(result)