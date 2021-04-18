str1 = input("Enter a string: ")
str = ""
for i in str1:
    if i not in str:
        str += i
print(str)