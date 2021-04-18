#Check if a Substring is Present in a Given String 

def check(str1, str2) :
    if (str1.count(str2) > 0 ) :
        print("String is Present")
    else :
        print("String is not Present")

str1 = input("Enter the first string :-")
str2 = input("Enter the second String :-")
check(str1, str2)

