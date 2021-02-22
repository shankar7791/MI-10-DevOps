#Python program to find the largest number amongst the tree numbers
a = int(input("Enter 1st number : "))
b = int(input("Enter 1st number : "))
c = int(input("Enter 1st number : "))
if a > b and  a > c :
    p = a
elif b > c and b > a :
    p = b
else :
    p = c
print(f"{p} is largest number .")            
    