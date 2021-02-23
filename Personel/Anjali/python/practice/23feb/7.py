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

'''
while i >= 0 :
    if (('A' <= var <= 'Z')) or (('a' <= var <= 'z')) :
        lc = lc + 1
    else :
        dc = dc + 1
'''