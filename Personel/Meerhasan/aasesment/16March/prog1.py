
# Python program to interchange first and last elements in a list 

list = [24,12,34,25,51,10]
start, *middle, end = list
list = [end, *middle, start]
print(list)
