# Program 4 : Write a Python program to count the number of even and odd numbers 
# from a series of numbers.

num1=int(input("Enter the starting number of series : "))
num2=int(input("Enter the ending number of series : "))
even=odd=0
temp_num1=num1
while num1<=num2 :
    if num1%2==0 :
        even +=1
    else :
        odd +=1
    num1 +=1

print(f"Even number count from series {temp_num1} to {num2} is : {even}")
print(f"Odd number count from series {temp_num1} to {num2} is : {odd}")