class queue:
    def __init__(self,length):
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
        self.rear = (self.rear+1) % self.len
        self.list[self.rear] = item
        self.size += 1
        print(f"{item} is enqueue from queue ")
    
    def dequeue(self,item):
        if self.empty():
            print("List is Empty ")
            return 
        self.front = (self.front + 1) % self.len
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
queue.enqueue(10)
queue.enqueue(20)
queue.enqueue(30)
queue.enqueue(40)
queue.dequeue(10)
queue.que_front()
queue.que_rear()
