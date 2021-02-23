# Program to add natural numbers up to n
n = int(input("Enter the number : "))
sum = 0
i = 1

while i <= n:
    sum = sum + i
    i = i+1

print("The sum is : ", sum)
