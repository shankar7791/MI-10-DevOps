
# Given a string, find all the duplicate characters which are similar to each others.

string = input("Enter a string : ")

duplicates = []
for char in string :
  
   if string.count(char) > 1 :

        if char not in duplicates :
            duplicates.append(char)
       
print(*duplicates)





