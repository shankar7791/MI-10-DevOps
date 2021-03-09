#Program to count vowels,consonant,digits and special character in a given string. 
  
def countStr(str): 
    vowels = 0
    consonant = 0
    specialChar = 0
    digit = 0
    space = 0
  
    for i in range(0, len(str)):            
        ch = str[i]  
        if ( (ch >= 'a' and ch <= 'z') or (ch >= 'A' and ch <= 'Z') ):  
            ch = ch.lower() 
            if (ch == 'a' or ch == 'e' or ch == 'i' or ch == 'o' or ch == 'u'): 
                vowels += 1
            else: 
                consonant += 1          
        elif (ch >= '0' and ch <= '9'): 
            digit += 1
        elif ch==" " :
            space=space+1
        else: 
            specialChar += 1
      
    print("Vowels : ", vowels) 
    print("Consonants : ", consonant)  
    print("Digits : ", digit)  
    print("Special Characters : ", specialChar)  
    print("Spaces : ", space) 
  
str = input("Enter the string : ")
countStr(str)
  
