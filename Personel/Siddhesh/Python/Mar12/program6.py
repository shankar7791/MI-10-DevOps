#Convert a list of characters into a string
#Input : ['p', 'r', 'o', 'g', 'r', 'a', 'm', 'm', 'i', 'n', 'g']
                       
#Output : programming

def convert(char):
    list = ""
    for i in char:
        list += i
    return list

char = list(input("enter the list : "))
print(char)
print(convert(char))

