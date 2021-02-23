#program that accepts a string and calculate the number of digits and letters.

string = (input("Enter string:"))
count1=0
l=len(string)
for i in string:
    if(i.isdigit()):
        count1=count1+1
     
print("The number of digits is:",count1)
print(count1)
print("The number of characters is:",l)
