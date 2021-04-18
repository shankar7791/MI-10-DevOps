#program to print the pascal's  triangle
n =int(input("Enter the number of rows : "))
list1=[]
for i in range(n):
    temp=[]
    for j in range(i+1):
        if j==0 or j==i:
            temp.append(1)
        else:
            temp.append(list1[i-1][j-1] + list1[i-1][j])
    list1.append(temp)
    
for i in range(n):
    for j in range(n-i-1):
        print(format(" ","<2") ,end="")
    for j in range(i+1):
        print(format(list1[i] [j],"<3") ,end=" ")
    print()
