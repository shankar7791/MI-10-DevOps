
# pascal triangle
def pascal_triangle(P):
    a = [[] for i in range(P)]
    for i in range(P):
        for j in range(i+1):
            if (j < i):
                if(j == 0):
                    a[i].append(1)
                else:
                    a[i].append(a[i-1][j]+a[i-1][j-1])
            elif(j == i):
                a[i].append(1)
    return a


P = 5
print(pascal_triangle(P))
