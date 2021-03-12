# Program 1 : Program to accept the strings which contains all vowels using set

def check(string):
    if len(set(string.lower()).intersection("aeiou")) >= 5:
        return ("String is accepted")
    else:
        return ("String is not accepted")
 
string = input("Enter the string : ")
print(check(string))