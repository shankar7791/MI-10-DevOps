#Convert a list of characters into a string
#Input : ['p', 'r', 'o', 'g', 'r', 'a', 'm', 
#                        'm', 'i', 'n', 'g']

def convert(str1):
    new = ""
    for char in str1 :
        new += char

    return new

str1 = ['p', 'r', 'o', 'g', 'r', 'a', 'm', 'm', 'i', 'n', 'g']
print(convert(str1))