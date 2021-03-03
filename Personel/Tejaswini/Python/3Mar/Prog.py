# Program to add two matrices using nested loop
R = int(input("Enter the number of rows:")) 
C = int(input("Enter the number of columns:")) 
M1=[]
M2=[]
sum=[]

print("Enter the First Matrix:") 
  
# For user input First Matrix
for i in range(R):          # A for loop for row entries 
    a =[] 
    for j in range(C):      # A for loop for column entries 
         a.append(int(input())) 
    M1.append(a) 
  
# For printing the matrix 
print("First Matrix is for M1:")
for i in range(R): 
    for j in range(C): 
        print(M1[i][j], end = " ") 
    print() 

# For user input Second Matrix
print("Enter the Second Matrix:") 
for i in range(R):          # A for loop for row entries 
    b =[] 
    for j in range(C):      # A for loop for column entries 
         b.append(int(input())) 
    M2.append(b) 
  
# For printing the matrix 
print("Second Matrix is for M2:")
for i in range(R): 
    for j in range(C): 
        print(M2[i][j], end = " ") 
    print() 
    
#Addition
sum=[[0 for i in range(C)] for i in range(R)]

for i in range(R):
    for j in range(C):
        sum[i][j] = M1[i][j]+M2[i][j]

print("\nThe Sum of two Matrices is : ")
for r in sum:
    print(r)