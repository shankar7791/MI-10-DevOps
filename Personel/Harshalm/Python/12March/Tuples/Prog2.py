#Convert a list of characters into a string


def convert(string) :
    new = " "

    for x in string :
        new += x

    return new

n = int(input("Enter the number of list :-"))
l = []
for i in range(0,n) :
    print("Enter item at index", i)
    item = input()
    l.append(item)
print("user listed is ", l)

print("the string is coverted from given list :-")
convert(l)

