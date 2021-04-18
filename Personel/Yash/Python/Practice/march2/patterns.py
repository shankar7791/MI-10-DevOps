rows=int(input("Enter the no of rows : "))  #5
for i in range(1,rows+1) :
    for j in range(1,i+1) :
        print("*",end=" ")
    print()
'''
* 
* * 
* * * 
* * * * 
* * * * * 
'''

for i in range(1,rows+1,2) :
    for j in range(1,i+1) :
        print("*",end=" ")
    print()
'''
* 
* * * 
* * * * *
'''

for i in range(1,rows+1) :
    for j in range(1,i+1) :
        print(i,end=" ")
    print()
'''
1 
2 2 
3 3 3 
4 4 4 4 
5 5 5 5 5 
'''

for i in range(1,rows+1) :
    for j in range(1,i+1) :
        print(j,end=" ")
    print()

'''
1 
1 2 
1 2 3 
1 2 3 4 
1 2 3 4 5 
'''

k=1
for i in range(1,rows+1) :
    for j in range(1,k+1) :
        print("*",end=" ")
    k=k+2
    print()

'''
* 
* * * 
* * * * * 
* * * * * * * 
* * * * * * * * * 
'''
