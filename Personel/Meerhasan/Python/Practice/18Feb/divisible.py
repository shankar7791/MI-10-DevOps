
# Write a program to check whether a number is divisible by 5 an 11 or not

num = int(input("Enter the number : "))

if num % 5 == 0 and num % 11 == 0 :
    print(f"{num} Is divisible by 5 or 11")
else :
    print(f"{num} Is not divisible by 5 or 11 ")