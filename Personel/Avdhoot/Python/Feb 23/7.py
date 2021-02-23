#Write a Python program that accepts a string and calculate the number of digits and letters

var = input("Enter a string ")

lc, dc = 0, 0
i = 0
while i < len(var) :
    if (var[i].isalpha()):
        lc += 1
    elif (var[i].isdigit()) :
        dc += 1
    else :
        pass
    i = i + 1

print("Letters", lc)
print("Digits", dc)