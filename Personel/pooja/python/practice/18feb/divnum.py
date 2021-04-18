 # Prog 4:  Write a program to check whether a number is divisible by 5 an 11 or not 
 
number =  int (input(" Enter the  positive number :"))
if ((number % 5 == 0) and (number % 11 == 0)):
     print("Given number {0}is divisible by 5 and 11 ". format(number))
else:
    print("Given number {0}is  not divisible by 5 and 11 ". format(number))