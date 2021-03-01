#Accept number from user and calculate the sum of all number between 1 and given number
sum = 0
n = int(input("Please enter number "))
for i in range(1, n + 1, 1):
    sum += i
print("\n")
print("Sum is: ", sum)