#program to accept the string which contains all string

def string():
    vowels=set("aeiou")

    a=input("Enter the string : ")
    s=set({})
    for i in a:

        if i in vowels:
            s.add(i)
    if(list(s)==list(vowels)):
        print("Accepted")
    else:
        print("Not accepted")
string() 