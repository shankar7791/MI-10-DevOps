def pali(str):
    str1=""
    for i in str:
        str1=i+str1
        print(f"string is in reverse {str1}")
    if str==str1:
        print("String is palindrome")
    else:
        print("String is not palindrome")

def symm(str):
    string= len(str)
    flag=0

    if string%2:
        mid=string//2 +1
    else:
        mid=string//2
    first=0
    second=mid

    while(first<mid and second <string):
        if (str[first]== str[second]): 
            first = first + 1
            second = second + 1
        else: 
            flag = 1
            break
       
    if flag == 0: 
        print("string is symmetrical") 
    else: 
        print("string is not symmetrical") 

str=input("Enter the string  ")
pali(str)
symm(str)