var1 = str(input("Enter a word "))
var2 = ''
i = len(var1) - 1

while(i>=0):
    var2 = var2 + var1[i]
    i = i - 1

print(var2)