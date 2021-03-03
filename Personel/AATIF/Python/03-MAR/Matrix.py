a = int(input("Enter the Number of Rows: "))

b = int(input("Enter the Number of Column: "))

matrix = []
for i in range(a) :
    c = []
    for j in range(b) :
        j = int(input("Enter First Matrix NUmber: "))
        c.append(j)
    matrix.append(c)

matrix1 = []
for i in range(a) :
    d = []
    for j in range(b) :
        j = int(input("Enter Second Matrix NUmber: "))
        d.append(j)
    matrix1.append(d)

print("First Matrix________")
for i in range(a) :
    for j in range(b) :
        print(matrix[i][j], end=" ")
    print()

print("Second Matrix________")
for i in range(a) :
    for j in range(b) :
        print(matrix1[i][j], end=" ")
    print()

result = [[0,0,0],[0,0,0],[0,0,0]]
for i in range(a) :
    for j in range(b) :
        result[i][j] = matrix[i][j] + matrix1[i][j]

print("Result Of Matrix_______________")
for i in range(a) :
    for j in range(b) :
        print(result[i][j], end=" ")
    print()