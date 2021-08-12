
# Write a program thats read a prefix exp and evaluates it.

class stack_cls :
    
    def __init__(self, element):
        self.stack = []
        self.element = element
        self.item = self.element.split(',')
        print(f"stack prefix element is : {self.item}")
        self.item = self.item[::-1]
        
    def push(self,i) :
        self.stack.append(i)

    def pop(self) :
        self.item = self.stack.pop()
        return int(self.item) 
    def main(self) :
        for i in self.item :
            if i.isdigit():
                self.push(i)
            elif i == '+':
                n1 = self.pop()
                n2 = self.pop()
                ans = n2 + n1 
                self.push(ans)
            elif i == '-':
                n1 = self.pop()
                n2 = self.pop()
                ans = n2 - n1 
                self.push(ans)
            elif i == '*':
                n1 = self.pop()
                n2 = self.pop()
                ans = n2 * n1 
                self.push(ans)
            elif i == '/':
                n1 = self.pop()
                n2 = self.pop()
                ans = n2 / n1 
                self.push(ans)        
    
    def show_stack(self):
        print(f"stack is : {self.stack}")
entry = input("enter the prefix element : ")

postfix = stack_cls(entry)
postfix.main()
postfix.show_stack()