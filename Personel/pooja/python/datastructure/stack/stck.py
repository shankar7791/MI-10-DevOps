#stack implementation in python


#creating stack 
def create_stack():
    stack=[]
    return stack
 
 #creating an empty stack
def check_empty(stack):
    return len(stack) == 0

# Adding items into stack
def push(stack,item):
    stack.append(item)
    print("pushed items:" + item)

def pop(stack):
    if(check_empty(stack)):
        return "stack is empty"



stack = create_stack()
push(stack,str(1))
push(stack,str(2))
push(stack,str(3))
push(stack,str(4))
print("popped item: " + pop(int(stack)))
print("stack after popping an element: " + int(stack))
