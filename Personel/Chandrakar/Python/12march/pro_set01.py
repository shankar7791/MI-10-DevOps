def check(string,string2):
    dict1 = set({})
    for  i in string :
        if i in string2:
            dict1.add(i)
        else:
            pass
    return dict1        
    
str1 = input("enter the string : ")
vowels = set("aeiou")
check(str1,vowels)    
st = check(str1,vowels)   
if len(st) == len(vowels):
    print("all Vowels are present ")
else :
        print("all Vowels are not present ")        