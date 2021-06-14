
#Implement que and perform Enque and Deque operations on queue.

class Que :
    def __init__(self, num1,num2,num3): 
        self.queue = []
        self.num1 = num1 
        self.num2 = num2
        self.num3 = num3
    def enqueu (self):
        self.queue.append(self.num1)
        self.queue.append(self.num2)
        self.queue.append(self.num3)
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
        if len(self.queue) == 1 :
            front = rear = None
        print(f"After dequeue opration values  : {self.queue}")
a = Que(2,3,4) 
a.enqueu()  
a.dequeue()     