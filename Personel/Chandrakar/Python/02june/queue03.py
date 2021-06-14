
# Implement queue size of 7 and shwo the
#   a. Size of queue
#   b. Check queue is Empty or not
#   c. Check queue is full or not

class Que :
    def __init__(self, num1,num2,num3,num4,num5,num6,num7): 
        self.queue = []
        self.num1 = num1 
        self.num2 = num2
        self.num3 = num3
        self.num4 = num4
        self.num5 = num5
        self.num6 = num6
        self.num7 = num7
    def enqueu (self):
        self.queue.append(self.num1)
        self.queue.append(self.num2)
        self.queue.append(self.num3)
        self.queue.append(self.num4)
        self.queue.append(self.num5)
        self.queue.append(self.num6)
        self.queue.append(self.num7)
        print(f"After enequeue opration values: {self.queue}")
        if len(self.queue) == 1 :
            front = rear = 0
            print(f"front and rear postion is : {front}")
        else :
            rear = len(self.queue) - 1
            print(f"rear position : {rear}")
    def dequeue (self):
        self.queue.pop(0)
        self.queue.pop(0)
        self.queue.pop(0)
        
        if len(self.queue) == 1 :
            front = rear = None
        print(f"After dequeue opration values  : {self.queue}")

    def isEmty(self):
            if len(self.queue) >= 1 :
                print("Not emty Queue")
            else :
                print("Emty Queue")  

    def size_Q(self):
            if len(self.queue) == 7 :
                print("Queue is full ")
            else :
                print("Queue is not full")                
a = Que(2,3,4,5,6,7,8) 
a.enqueu()  
#a.dequeue()     
a.isEmty()
a.size_Q()