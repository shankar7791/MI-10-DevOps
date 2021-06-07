
class queue:
    def __init__(self):
        self.queue = []
        self.max = 8
    def insert(self,item):
        if len(self.queue) < self.max:
            self.queue.append(item)
        else :
            print("Queue is full ")
    def full(self):
        if self.max == len(self.queue):
            print("Full : True ")
        else:
            print("Full : False")
    def empty(self):
        if len(self.queue) == 0:
            print("Empty : True ")
        else:
            print("Empty : False")
    def size(self):
        print("Size : ", len(self.queue))
    def delete(self):
        if (len(self.queue)) > 0:
            self.queue.pop()
        else:
            print("The queue is empty")
ob = queue()
while(True):
    print("""
    1 - Insert
    2 - To check full
    3 - To echeck empty
    4 - to check size
    5 - delete
    6 - exit
    """)

    ch = int(input("Enter the choice : "))
    if ch == 1:
        ob.insert(int(input("Enter the item : ")))
    elif ch == 2:
        ob.full()
    elif ch == 3:
        ob.empty()
    elif ch == 4:
        ob.size()
    elif ch == 5:
        ob.delete()
    elif ch == 6:
        exit()
    else:
        print("Invalid choice")






# from queue import Queue

# q = Queue(maxsize = 8)
# print("\nThe maximun size of queue : ",q.maxsize)

# print("\nThe size of the queue : ",q.qsize())


# q.put("E")
# q.put("L")
# q.put("A")
# q.put("N")
# q.put('K')
# q.put('A')
# q.put('V')
# q.put('I')

# print("\nfull : ",q.full())

# print("\n dequeued from queue :")
# print("\t",q.get(),q.get(),q.get(),q.get(),q.get(),q.get(),q.get(),q.get())

# print("\nEmpty : ",q.empty())

# q.put("i")

# print("\nfull :",q.full())
# print("\nEmpty : ",q.empty())