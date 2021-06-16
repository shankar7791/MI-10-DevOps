
#Implement que size of 7 and show the ,
#a.Size of queue.
#.Check queue is empty or not.
#.Check queuq is full or not.


class stack_cls :
    def __init__(self, num1, num2, num3): 
        self.stack = []
        self.num1 = num1  
        self.num2 = num2  
        self.num3 = num3  
    def insert_item(self) :         
        self.stack.append(self.num1)
        self.stack.append(self.num2)
        self.stack.append(self.num3)
    def delete_item(self):         
        self.stack.pop(0)               
        self.stack.pop(0)               

    def show_stack(self) :               
        return self.stack

s = stack_cls(2,3,4)               
s.insert_item()                    
print(f"insert stack values are  : {s.show_stack()}") 
s.delete_item()
print(f"after the delete stack values : {s.show_stack()}") 