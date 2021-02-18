#check the number is positive or negative or zero

num =int(input("Enter the number : "))
if(num > 0):
    print(f"The number {num} is positive")
elif(num<0):
    print(f"The number {num} is negative")
else:
    print(f"The number {num} is zero")