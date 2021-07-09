num = int(input("Enter the Number:"))
revrs = 0
while(num > 0):
    n = num % 10
    revrs = revrs * 10 + n
    num = num // 10
print("Entered Number Reversed: ", revrs)