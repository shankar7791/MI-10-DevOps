def is_operand(c):

    return c.isdigit()


def evaluate(exp):

	stack = []

	for c in exp[::-1]:

		if is_operand(c):
			stack.append(int(c))
			

		else:
			first = stack.pop()
			print(first)
			sec = stack.pop()
			print(sec)

			if c == '+':
				stack.append(first + sec)

			elif c == '-':
				stack.append(first - sec)

			elif c == '*':
				stack.append(first * sec)

			elif c == '/':
				stack.append(first / sec)
		print("stck",stack)
			

	return stack.pop()


exp = "+9*26"
print("The prefix evaluation : ",evaluate(exp))

