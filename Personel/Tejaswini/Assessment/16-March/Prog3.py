#Check if a Substring is Present in a Given String
              
str1 = input("Enter string : ")
substr = input("Enter substring : ")
if (str1.count(substr)>0):      
    print(f"YES, {substr}=> is present in =>{str1}")  
else:  
    print(f"NO, {substr}=> is not present in =>{str1} ")