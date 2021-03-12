# Program to accept the strings which contains all vowels

def check(string) :
 
    string = string.lower()

    vowels = set("aeiou")
 
    s = set({})
 
    for char in string :
 
        if char in vowels :
            s.add(char)
        else:
            pass
    if len(s) == len(vowels) :
        print("Accepted")
    else :
        print("Not Accepted")

string = input("Enter the string : ")
check(string)
