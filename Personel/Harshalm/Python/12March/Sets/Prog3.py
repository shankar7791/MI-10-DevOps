#Remove items from Set until set not become empty set

def remove(sets) :
    while sets :
        sets.pop()  #pop method
        print(sets)

num = set(input("Enter the sets element :-"))

remove(num)

