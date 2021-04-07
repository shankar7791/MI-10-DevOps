def matrix(arr,n):
    for i in range(n):
        for j in range(n):
            if i == 0:
                print(arr[i][j],end=" ")
            elif i == j:
                print(arr[i][j],end=" ")
            elif i == n -1:
                print(arr[i][j],end=" ")
a = [[1,2,3],
     [4,5,6],
     [7,8,9]]
matrix(a,3)


a = [[5,19,8,7],
     [4,1,14,8],
     [2,20,1,9],
     [1,2,55,4]]
matrix(a,4)