
# Remove empty tuples from a list


list1 = [(), 1, 2, (), 3, 4, 5, ()]
tup = filter(None, list1)
print(list(tup))