#Assignment Operator
# program to read a number and find the addition of the digits

num = int(input("Enter a number "))
if num < 0:
	print("Invalid Input")
else:
	sum = 0
	while	num > 0:
		digit = num % 10
		sum += digit
		num = num // 10
	print("sum = ",sum)