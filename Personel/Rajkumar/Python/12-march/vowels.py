#Program to accept the strings which contains all vowels
def str1():
    v=set("aeiou")

    a=input("Enter a string : ")
    s=set({})
    for i in a:
        if i in v:
            s.add(i)
    if(list(s)==list(v)):
        print("yes")
    else:
        print("Not")
str1() 