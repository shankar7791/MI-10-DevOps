# Python program to interchange first and last elements in a list

list1=[int(x) for x in input("Enter Input seprated by space: ").split()]
print("Original List:",list1)
list1[0], list1[-1] = list1[-1], list1[0]
print("Output: ",list1)