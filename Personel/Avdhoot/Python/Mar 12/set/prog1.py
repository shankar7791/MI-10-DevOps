#Program to accept the strings which contains all vowels
def str2(str1):
    str1 = str1.lower()
    ls = set("aeiou")
    ls1 = set({})
    

    for char in str1:
        if char in ls:
            ls1.add(char)
        else :
            pass

    if len(ls1) == len(ls):
        print(f"{str1} is Accepted")
    else :
        print(f"{str1} is not Accepted")


print(str2(input("Enter a string: ")))