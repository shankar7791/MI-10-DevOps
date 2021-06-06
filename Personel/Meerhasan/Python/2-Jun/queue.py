# queue FIFO


queue = []

for i in range(7) :
    queue.append(i)

print("Inserted Elements In A Queue : ", queue)

if len(queue) == 7 :
    print("Queue Is Full ")


print("\nPoped Element From Queue : ", queue.pop(0))
print("Queue : ", queue)

print("\nPoped Element From Queue : ", queue.pop(0))
print("Queue : ", queue)

print("\nPoped Element From Queue : ", queue.pop(0))
print("Queue : ", queue)

print("\nPoped Element From Queue : ", queue.pop(0))
print("Queue : ", queue)

print("\nPoped Element From Queue : ", queue.pop(0))
print("Queue : ", queue)

print("\nPoped Element From Queue : ", queue.pop(0))
print("Queue : ", queue)

print("\nPoped Element From Queue : ", queue.pop(0))
print("Queue : ", queue)


if len(queue) == 0 :
    print("\nQueue Is Empty ")

