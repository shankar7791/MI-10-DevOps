# Python program to interchange first and last elements in a list

list = []

n = int(input("Enter the number of elements in list:"))

for x in range(0, n):

    element = input("Enter element:")
    list.append(element)

print("Your current list is:", list)
temp = list[0]
list[0] = list[n-1]
list[n-1] = temp

print("New list is:", list)