#program to calculate sum of a list of numbers using recursion :

# Algorith :
# 1: Assign i =0 and a function as add
# 2:Take input from user as var n
# 3:use condition statement 
# 4:If conditional is true execute the statement
# 5:else return 0
# 6:finally return the if statement value and print the value
# 7:call the function


i=0
def add(n):
   
    if i<=n:
        sum=add(n-1)+n
    else:
        return 0
    return sum
n = int(input("Enter numbers : "))
print("sum is = ",add(n))
add(n)