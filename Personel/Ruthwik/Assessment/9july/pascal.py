# Python Program to Print the Pascal’s triangle for n number of rows given by the user

num=int(input("Enter number of rows: \n"))
def pas(n):
    t=[]
    for i in range(n):
        t.append([])
        t[i].append(1)
        for j in range(1,i):
            t[i].append(t[i-1][j-1]+t[i-1][j])
        if(n!=0):
            t[i].append(1)
    for i in range(n):
        print("   "*(n-i),end=" ",sep=" ")
        for j in range(0,i+1):
            print('{0:6}'.format(t[i][j]),end=" ",sep=" ")
        print()

pas(num)