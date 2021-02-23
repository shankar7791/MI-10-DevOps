#Write a Python program that accepts a word from the user and reverse it.
var = str(input("Enter a word "))
var2 = ''
i = len(var) - 1

while(i>=0):
    var2 = var2 + var[i]
    i = i - 1

print(var2)