#Write a Python program to solve the Fibonacci sequence using recursion
'''
Algorithm
1. Define a Function
2. If num is less than equal to 1 then goto step 3 otherwise goto step 4
3. Write num
4. Do the recursion
5. Take the user input 
6. If number is less than equal to 0 then goto step 7 otherwise goto step 8
7. Print "Enter positive number"
8. Print the series using for loop
'''
def fibo(num):
    if num <= 1 :
        return num
    else :
        return (fibo(num - 1) + fibo(num - 2))


a = int(input("Enter the number: "))
if a <= 0:
   print("Plese enter a positive integer")
else:
   print("Fibonacci sequence:")
   for i in range(a):
       print(fibo(i))