


string = input("Enter a string : ")
output = ""
for i in string :
    if i not in output : 
        output = output + i
print("Result after removing the duplicates characters :", output)