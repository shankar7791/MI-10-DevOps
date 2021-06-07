class PreFix:
    def __init__(self):
        self.items = []
 
    def is_empty(self):
        return self.items == []
 
    def push(self, data):
        self.items.append(data)
        
    def pop(self):
        return self.items.pop()

    def print(self):
        for i in self.items:
            print(i)
            

    def doMath(self,op, op1, op2):
        if op == "^":
            return op1 ** op2
        if op == "*":
            return op1 * op2
        elif op == "/":
           return op1 / op2
        elif op == "+":
            return op1 + op2
        else:
            return op1 - op2  
    
    def prefix(self, val):

        tokenList = val.split(' ')
        
        for token in tokenList[::-1]:
            
            try:
                self.push(int(token))
            except:
                operand2 = self.pop()
                operand1 = self.pop()
                result = self.doMath(token,operand1,operand2)
                self.push(result)

        return self.pop()

pf = PreFix()

val = input("\n\nEnter PostFix expression with spaces :")

print('\n',pf.prefix(val))

