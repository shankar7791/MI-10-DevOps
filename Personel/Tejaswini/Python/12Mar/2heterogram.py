#Check Whether a string is Heterogram or Not

def heterogram(str1):
    char = [ch for ch in str1 if (ord(ch) >= ord('a') and ord(ch) <= ord('z'))]
    if len(set(char)) == len(str1):
        print("Yes, Sting is Heterogram")
    else:
        print("String is not Heterogram")

str1 = input("Enter string : ")
heterogram(str1)