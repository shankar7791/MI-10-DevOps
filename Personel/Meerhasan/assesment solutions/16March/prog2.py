
# Program to print duplicates from a list of integers


list = [1,2,3,4,5,1,2,4]

duplicates = []
for i in list :
  
   if list.count(i) > 1 :

        if i not in duplicates :
            duplicates.append(i)
print(f"{list}\n")
print("duplicates values from the given list : ",*duplicates)