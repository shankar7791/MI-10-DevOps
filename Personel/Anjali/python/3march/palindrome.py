def pali(str):
    str1=""
    for i in str:
        str1=i+str1
        print(f"string is in reverse {str1}")
    if str==str1:
        print("String is palindrome")
    else:
        print("String is not palindrome")
str=input("Enter the string  ")
pali(str)