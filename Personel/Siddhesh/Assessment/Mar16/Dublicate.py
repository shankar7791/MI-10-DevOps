#Program to print duplicates from a list of integers


lst = [ -1, 1, -1, 8]
dupItems = []
uniqItems = {}
for x in lst:
   if x not in uniqItems:
      uniqItems[x] = 1
   else:
      if uniqItems[x] == 1:
         dupItems.append(x)
      uniqItems[x] += 1
print(dupItems)


