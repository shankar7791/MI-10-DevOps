#Remove all duplicates from a given string in Python
def remove():
    str1=input("Enter the string")
    str=""
    for i in str1:
        if i not in str:
            str=str+i
    print(str)
remove()