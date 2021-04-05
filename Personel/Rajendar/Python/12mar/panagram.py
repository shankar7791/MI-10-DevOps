import string
alphabet = set(string.ascii_lowercase)


def panagram(string):
    return set(string.lower()) >= alphabet


string = input(" enter the string :")
if(panagram(string) == True):
    print("it is panagram")
else:
    print(" it is not a panagram")
