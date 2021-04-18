# Remove all duplicates from a given string in Python 

string = input("Enter a string : ")
output = ""
for i in string :
    if i not in output : 
        output = output + i
print("Original string : ", string)
print("Result after removing the duplicates characters :", output)

