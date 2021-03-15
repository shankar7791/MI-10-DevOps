def par_g(str4,str2):
    flag = True
    for char in str4:
        if char not in str2:
            flag = False

    if(flag ==True ):
        print("pangram")
    else :
        print("not pangram ")            
str1 = input("enter the strings : ")
str2 = set(str1)
str3 ="abcdefghijklmnopqrstuvwxyz"
str4 = set(str3)
print(str4)
par_g(str4,str2)