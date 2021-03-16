#Python program to interchange first and last elements in a list

def interchange(list) :

    list[0] , list[-1] = list[-1] , list[0]

    return list

list = [i for i in input("Enter the list element :-").split()]
print("Input List :-", list)
print("Ouput list :-", list)
interchange(list)


