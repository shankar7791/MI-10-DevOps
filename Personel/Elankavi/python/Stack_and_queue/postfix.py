def operators(c):
    return c.isdigit()

def evaluate(arr):
    stack = []
    for c in arr:
        
        if operators(c):
            stack.append(int(c))
        else:
            first = int(stack.pop())
            sec = int(stack.pop())
            if c == "+":
                stack.append(sec + first)

            elif c == "-":
                stack.append(sec - first)
            elif c == "*":
                stack.append(sec * first)
            elif c == "/":
                stack.append(sec / first)
            elif c == "%":
                stack.append(sec % first)
    return stack[-1]

arr = "123+-65/78%"
b = evaluate(arr)
print("protfix evaluation :",b)