# Program to accept the chs which contains all vowels

def vow_check(ch) :
 
    ch = ch.lower()
    vowels = set("aeiou")
    s = set({})
 
    for char in ch :
 
        if char in vowels :
            s.add(char)
        else:
            pass
             
    if len(s) == len(vowels) :
        print("Accepted")
    else :
        print("Not Accepted")
 
 
a = input('Enter a string : ')

if len(a) > 0:
    vow_check(a)