# WAP to accepts a string and calculate the no of digits and letters.

var = input("Enter a string ")

dc = 0

lc = 0

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

    © 2021 GitHub, Inc.
    Terms
    Privacy
