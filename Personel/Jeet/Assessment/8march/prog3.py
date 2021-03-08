#Python Program for Program to add Matrix in Z form

m = []
row = int(input('enter no of row:'))
col = int(input('enter no of column:'))

for i in range(row):
    a = []
    for j in range(col):
        k = int(input(f'enter value of {i} row:'))
        a.append(k)
    m.append(a)

add = 0
for i in range(1):
    for j in range(col-1):
        add += m[i][j]
k=1
for i in range(row):
    for j in range(col-1,-1,-1):
        if j == col-k:
            add += m[i][j]
            break
    k+=1


for i in range(row-1,row-2,-1):
    for j in range(1,col):
        add += m[i][j]
print(add)