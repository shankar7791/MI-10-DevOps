# Program 4 : Python program to find the sum of sequence of all numbers upto the given number using recursive function

def getsum(n):
    if(n <= 0):
        return n
    else:
        return n + getsum(n-1)


n = int(input("enter the number :"))
print(getsum(n))

# ALGORITHM
# 1 take input from user in function
# 2 declare function
# 3 using if loop check n is greater than 0
# 4 return the number
# 5 else return addition of given number and minus given number
# 6 print result using function
