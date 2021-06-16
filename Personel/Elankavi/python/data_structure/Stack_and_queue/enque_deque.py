class queue:
    def __init__(self,length):
        print(length)
        self.len = length
        self.rear = length - 1
        self.front = 0
        self.size = 0
        self.list = [None] * length

    def full(self):
        return self.size == self.len
    def empty(self):
        return self.size == 0

    def enqueue(self,item):
        if self.full():
            print("List is full ")
            return
        print("before",self.rear)
        self.rear = (self.rear+1) % self.len
        print("after",self.rear )
        self.list[self.rear] = item
        self.size += 1
        print(f"{item} is enqueue from queue ")
    
    def dequeue(self,item):
        if self.empty():
            print("List is Empty ")
            return 
        self.front = (self.front + 1) % self.len
        print(self.front)
        self.list[self.front] = item
        self.size -= 1
        print(f"{item} is dequeue from queue ")


    def que_front(self):
            if self.empty():
                print("Queue is empty")
            print("Front item is", self.list[self.front])
            
    def que_rear(self):
            if self.empty():
                print("Queue is empty")
            print("Rear item is",  self.list[self.rear])



queue = queue(5)
queue.enqueue(6)
queue.enqueue(0)
queue.enqueue(3)
queue.enqueue(90)
queue.dequeue(870)
queue.que_front()
queue.que_rear()
