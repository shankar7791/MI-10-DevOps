#Write a Python program to count the number of even and odd numbers from a series of numbers.

print("Enter the range ")
num1 = int(input("Enter Lower Limit "))
num2 = int(input("Enter Upper Limit "))

even, odd = 0, 0

while num1 <= num2 :
    if (num1 % 2 == 0) :
        even += 1
    else :
        odd += 1
    num1 = num1 + 1
    
print("Even no.", even)
print("Odd no.", odd)