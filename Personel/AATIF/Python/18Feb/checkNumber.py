#Program to check wether the number is positive, negative or zero.

num = float(input("Enter a number: "))
if num >= 0:
   if num == 0:
       print(f"\n{num}\nZero")
   else:
       print(f"\n{num}\nPositive number")
else:
   print(f"\n{num}\nNegative number")