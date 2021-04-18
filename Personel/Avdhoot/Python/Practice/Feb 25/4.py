num = int(input("Enter the digit "))

sum = 0
while num > 0 :
    digit = num % 10
    sum = sum + digit
    num = num // 10
print(sum)