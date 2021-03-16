# Program 3 : Check if a Substring is Present in a Given String 

str = input("Enter the string : ")
sub_str = input("Enter the substring : ")

# if (str.count(sub_str)>0):      
#     print("YES")  
# else:  
#     print("NO")  
if str.find(sub_str) == -1 :
    print("Substring is Not Present in a Given String")
else :
    print("Substring is Present in a Given String")