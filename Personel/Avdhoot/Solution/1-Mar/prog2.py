num = int(input("How many terms? "))

n1, n2 = 0, 1
count = 0

if num <= 0:
   print("Please enter a +ve integer")
elif num == 1:
   print(n1)
else:
   while count < num:
       print(n1)
       num1 = n1 + n2
       n1 = n2
       n2 = num1
       count += 1