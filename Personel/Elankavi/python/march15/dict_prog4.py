# Given a string find the duplicate character which are similare to each other

s=str(input("Enter the string : "))
print(s)
duplicates=[]
for i in s:
    if s.count(i)>1:
        if i not in duplicates:
            duplicates.append(i)
print("The duplicate words are : ",duplicates)