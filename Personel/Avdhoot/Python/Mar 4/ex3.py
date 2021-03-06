#Write a Python function that accepts a string and 
#calculate the number of upper case letters and lower case letters

def string(str1):
    uc,  lc =  0, 0
    for i in str1 :
        if i.isupper() :
            uc += 1
        elif i.islower():
            lc += 1
        else :
            pass
    print("Original string: ", str1)
    print("Number of upper-case: ",  uc)
    print("Number of lower-case: ",  lc)
string(input("Enter the string: "))
