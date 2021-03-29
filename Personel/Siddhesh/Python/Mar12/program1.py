#Program to accept the strings which contains all vowels


def check (string):

    string = string.lower()

    vowel= set("aeiou") 

    s = set({})

    for char in string :

        if char in vowel :
            s.add(char)
        else:
            pass
    if len(s) == len(vowel) :
        print("Accepted")  
    else :
        print("not Accepted") 


string = input("Enter the string: ")
check(string)


