#Python Program for Program to Print Matrix in Z form 

arr =[[1,2,3],
      [4,5,6],
      [7,8,9]]

num = len(arr[0])
i = 0
for j in range(0, num-1):
    print(arr[i][j], end = "")

k=1
for i in range(0,num)