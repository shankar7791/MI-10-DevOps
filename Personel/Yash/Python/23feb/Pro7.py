# Program 7 : Write a Python program that accepts a string and calculate the number of digits and 
# letters.
'''
s = input("Enter the string : " )
digits=letters=0
for i in s:
    if i.isdigit():
        digits=digits+1
    elif i.isalpha():
        letters=letters+1
print("Number of Letters", letters)
print("Number of Digits", digits)
'''

str1 = input("Enter a string: ")
dig=0
alp=0
i=0
l=len(str1)
while i<l:
    if str1[i].isdigit():
        dig =dig +1
    elif str1[i].isalpha():
        alp = alp +1
    else:
        print(f"Other than letter and digit are {str1[i]}")
    i=i+1

print(f"Total Digits are : {dig}")
print(f"Total Letters are : {alp}")