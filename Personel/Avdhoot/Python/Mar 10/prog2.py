#swap the first 2 leters of string

str1 = "abc"
str2 = "xyz"

a = str1[0:2]
b = str2[0:2]

a, b = b, a
print("String before swap :", str1 , str2)
print("String after swap :", f"{a}c",f"{b}z")