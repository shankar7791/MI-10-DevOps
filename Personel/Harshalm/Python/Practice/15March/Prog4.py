# Given a string, find all the duplicate characters which are similar to each others.

string = input("Enter the string :-")

duplicates = {}   # initializing a dictionary
for char in string :
    if char in duplicates :
        duplicates[char] += 1
    else :
        duplicates[char] = 1
for key, value in duplicates.items():
    if value > 1 :
        print(key, end = " ")
print()
