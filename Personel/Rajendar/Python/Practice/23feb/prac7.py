# Program 7 : Write a Python program that accepts a string and calculate the number of digits and letters.

str1 = input("Enter a string: ")
dig = 0
alp = 0
i = 0
l = len(str1)
while i < l:
    if str1[i].isdigit():
        dig = dig + 1
    elif str1[i].isalpha():
        alp = alp + 1
    else:
        print(f"Other than letter and digit i.e = {str1[i]}")
    i = i+1

print(f"Digits = {dig}")
print(f"Letters = {alp}")
