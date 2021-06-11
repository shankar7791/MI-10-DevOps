import collections
  
de = collections.deque([1,2,3])
print(de)

de.append(4)
print ("The deque after appending at right is : ")
print (de)
  
de.appendleft(6)
print ("The deque after appending at left is : ")
print (de)
  
de.pop()
print ("The deque after deleting from right is : ")
print (de)
  
de.popleft()
print ("The deque after deleting from left is : ")
print (de)

de.extend([4,5,6])
print ("The deque after extending deque at end is : ")
print (de)

de.extendleft([7,8,9])
print ("The deque after extending deque at beginning is : ")
print (de)

print ("The deque after all operation ")
print (de)
  