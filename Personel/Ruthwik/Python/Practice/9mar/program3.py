# Reverse the string and chech palindrome


def reverse() :
    temp_str =""
    for i in str :
        temp_str=i+temp_str
    return temp_str

str=input("Enter the string : ")
print(f"The reverse of string is : {reverse()}")

if str==(reverse()):
    print("Palindrome")
else :
    print("Not Palindrome") 