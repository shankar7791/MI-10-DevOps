# K shape pattern program
n=int(input("enter rows : "))

def kpat(n):
    for i in range(n):
        for j in range(n):
            if j == 0 or i - j == 3 or i + j == 3:
                print("*", end="")
            else:
                print(end=" ")
        print() 

kpat(n)