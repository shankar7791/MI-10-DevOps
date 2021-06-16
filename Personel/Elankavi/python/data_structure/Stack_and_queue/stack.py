
stack = []
print(" After insert Stack ")
def stack_insert():
    stack.append(5)
    stack.append(9)
    stack.append(6)

    print(stack)
    print("--------------------------------------------------------------------------------------")

def stack_delete():
    print(" After delete Stack ")
    stack.pop()
    stack.pop()
  
    print(stack)

stack_insert()


stack_delete()

