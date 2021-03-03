#[1, 2, 3],
# [4, 5, 6],
# [7, 8, 9]


def matrix(m, n):
    o = []
    for i in range(m):
        row = []
        for j in range(n):
            inp = int(input(f"enter o[{i}][ {j}]"))
            row.append(inp)
        o.append(row)
    return o
#[1, 2, 3], [4, 5, 6], [7, 8, 9]


def sum(A, B):
    output = []
    for i in range(len(A)):             # number of rows
        row = []
        for j in range(len(A[0])):        # number of column
            row.append(A[i][j] + B[i][j])
        output.append(row)
    return output


m = int(input("enter the value of m\n"))
n = int(input("enter the value of n\n"))

print(" enter matrix A")
A = matrix(m, n)
print(A)

print(" enter the matrix B")
B = matrix(m, n)
print(B)

s = sum(A, B)
print(s)
