#Python program to interchange first and last elements in a list

myList = [11, 23, 54, 35, 48, 25]
print(myList)
first = myList.pop(0)
last = myList.pop(-1)

myList.insert(0,last)
myList.append(first)

print("List after interchanging first and last elements in list\n",myList)