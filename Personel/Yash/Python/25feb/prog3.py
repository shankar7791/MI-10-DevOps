# Program 3 : Write a Python program to reverse the digits of a given number and 
# add it to the original, If the sum is not a palindrome repeat this procedure. 

num=int(input("Enter the number : "))
count=num
while True :
    str_num =str(num)
    rev_str=str_num[::-1]
    if str_num==rev_str :
        print(f"{num} is palindrome when entered number is {count}")
        break
    num=int(str_num)+int(rev_str)  

