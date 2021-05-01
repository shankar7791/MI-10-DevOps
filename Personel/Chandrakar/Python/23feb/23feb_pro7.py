#Write a Python program that accepts a string and calculate the number of digits and letters.
var = input("enter a string ")
dc = 0
lc = 0
i = 0
while i < len(var) :
    if (var[i].isalpha()) :
        lc = lc + 1
    elif (var[i].isdigit()):
        dc = dc +1
    else :
        pass
    i = i + 1
print("latter", lc)
print("digits", dc)                