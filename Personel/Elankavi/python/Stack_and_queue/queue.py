queue = []

queue.append("a")
queue.append("d")
queue.append("b")
queue.append("a")

print("After Insert : ")
print(queue)

print("-------------------------------------------------------------------------------------------------------")
 
queue.pop()
queue.pop(0)
queue.pop()

print("After delete ")
print(queue)