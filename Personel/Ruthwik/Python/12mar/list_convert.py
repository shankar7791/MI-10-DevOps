# Convert a list of characters into a string

def string_con(string):

    str1 = ""

    for x in string :
        str1 += x

    return str1


n = int(input('Enter number of elements in the list:'))
l = []
for i in range(0, n):
    print("Enter item at index", i )
    item = input()
    l.append(item)
print("User list is ", l)

print('The string converted from given list is : \n', string_con(l))