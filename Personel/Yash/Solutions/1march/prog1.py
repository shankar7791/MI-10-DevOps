# Program 1 : Print the following pattern using while loop 

num=int(input("Enter the no of rows : "))
i=num
while i>=1:
    j=i
    while j>= 1:
        print(j,end=" ")
        j=j-1
    print()
    i=i-1

