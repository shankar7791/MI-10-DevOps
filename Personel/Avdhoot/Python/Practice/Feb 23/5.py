#find the sum of n natural numbers

a = int(input("Enter a number "))

i = 1
sum = 0

while i <= a :
    sum += i
    i = i + 1
print(sum)