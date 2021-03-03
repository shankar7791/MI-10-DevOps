def palind(str1):
    str2=""
    l=len(str1)
    for i in str1:  
        str2 = i + str2
    if str1 == str2:
        print("\nString is Palindrome")
    else:
        print("\nString is not Plaidrome")


def symment(str1):
    l = len(str1) 
    flag = 0
    if l%2 == 0: 
        mid = l//2 
    else: 
        mid = l//2 + 1 
        
    s1 = 0  
    s2 = mid 
    
    while(s1 < mid and s2 < l): 
        
        if (str1[s1] == str1[s2]): 
            s1 = s1 + 1
            s2 = s2 + 1
        else: 
            flag = 1
            break
    
    if flag == 0: 
        print("\nThe entered string is symmetrical") 
    else: 
        print("\nThe entered string is not symmetrical") 

str1 = input("Enter a string:")
palind(str1)

symment(str1)