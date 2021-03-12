# Remove items from Set until set not become empty set

def setr(list1):

    set1 = set(list1)
    print(f'The set converted from list is : {set1}')

    print('The removal of set items : ')
    while set1 :
        set1.pop()
        print(set1)


n = int(input('Enter number of elements in the list:'))
l = []
for i in range(0, n):
    print("Enter item at index", i )
    item = input()
    l.append(item)
print("User list is ", l)

setr(l)