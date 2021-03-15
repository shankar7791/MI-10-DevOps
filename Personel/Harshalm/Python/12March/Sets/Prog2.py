 #Check whether a given string is Heterogram or not

def heterogramCheck(string) :

    alphabets = [ch for ch in string if (ord(ch) >= ord('a') and ord(ch) <= ord('z'))]

    if len(set(alphabets)) == len(alphabets) :
        print("It is a Heterogram")
    else :
        print("It is not a Heterogram")

str = input("Enter the string :-")

heterogramCheck(str)

