# stack implement insert and delete
  

class stack_cls :
    def __init__(self, num1, num2, num3):  # init method is class constructor pass the three parameter 
        self.stack = []
        self.num1 = num1  
        self.num2 = num2  
        self.num3 = num3  
    def insert_item(self) :         #take one method that is insert_item,here three values insert in stack
        self.stack.append(self.num1)
        self.stack.append(self.num2)
        self.stack.append(self.num3)
    def delete_item(self):          #delete_item method that is delete the last index values
        self.stack.pop()               #delete the index[2] value
        self.stack.pop()               #delete the index[1] value

    def show_stack(self) :         #show_stack method is return the stack        
        return self.stack

s = stack_cls(2,3,4)               #create one object that is s and pass the three argument 
s.insert_item()                    #inset_item method is call
print(f"insert stack values are  : {s.show_stack()}") #show_stack  method is call
s.delete_item()
print(f"after the delete stack values : {s.show_stack()}") #again show_stack method call 