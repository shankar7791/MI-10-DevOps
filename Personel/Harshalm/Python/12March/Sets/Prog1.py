#Program to accept the strings which contains all vowels

def vowelCheck(character) :
    character = character.lower()
    vowel = set("aeiou")
    s = set({})

    for char in character :

        if char in vowel :
            s.add(char)
        else :
            pass

    if len(s) == len(vowel) :
        print("Accepted")
    else :
        print("Not Accepted")

str = input("Enter the string :-")

if len(str) > 0 :
    vowelCheck(str)

    