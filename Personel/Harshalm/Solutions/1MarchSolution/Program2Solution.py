#write a program for Fibonacci series.


num = int(input("Enter the number :-"))

count = 0
num1 = 0
num2 = 1

if num <= 0 :
    print("Fibonacci series :-")
elif num == 1 :
    print("Fibonacci series :-" , num)
    print(num1)
else :
    print("Fibonacci series :-")
    while count < num :
        print(num1)
        sum = num1 + num2
        num1 = num2
        num2  = sum
        count += 1
