#program to slove the fibonacci sequence using recursion :

# Alogorithm
# 1: Take input as no of digits from the user
# 2: Assign an function as fibonacci
# 3: using the conditional statement
# 4: if conditional is True execute the statement
# 5: else execute the else statement and return the value
# 6: using for loop for the range to print the sequence.


a=int(input("How many digits : "))
def fibonacci(i):
    if i<=1:
        return i
    else:
        return(fibonacci(i-1) + (fibonacci(i-2)))
print("Fibonacci sequence is : ")
for i in range(a):
    print(fibonacci(i) , end=" ")
print()