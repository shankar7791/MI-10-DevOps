#Write a Python program to get the factorial of a number using recursion

#algorithm for following program 

"""
1. define the variable and take value from user.
2. def or create the function and on that function pass the parameter.
3. define if statement 
4. inside the if statement use recursive method
5. conditional statement : else statement : return condition
6. calling function
7. print statement 

"""
num = int(input("Enter a number : "))
def addSeq(num):
    if num >1 : 
        result = num * addSeq(num - 1)
    else :
        return 1     
    return result
print(addSeq(num))
print("is factorial of number")
