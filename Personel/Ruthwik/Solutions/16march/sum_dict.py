# Python program to find the sum of all items in a dictionary

def sum_dict(dict):
   sum_ = 0
   for i in dict.values():
      sum_ = sum_ + i
   return sum_
# Driver Function
dict = {}
n=int(input('enter no. of elements: '))
for i in range(n):
	key = input("Enter key :")
	value = input("Enter value :")
	dict[key] = int(value)

print('dict = ', dict)
print("Sum of dictionary values :", sum_dict(dict))