#Python set to check if string is panagram

def panagramCheck(string) :
    
    string = string.lower()
    string = set(string)

    alphabets = [ ch for ch in string if (ord(ch) in range(ord('a'), ord('z') + 1))]

    if len(alphabets) == 26 :
        print("It is Panagram")
    else :
        print("It is not a Panagram")

str = input("Enter the string :-")

panagramCheck(str)

