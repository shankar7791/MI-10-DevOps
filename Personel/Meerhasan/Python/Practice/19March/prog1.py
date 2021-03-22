
# Program for showing student mask using array

import array as a

maths = a.array("i", [0,56,70,20,44,76,59,67,76,54])

eco = a.array("i", [0,87,45,68,45,32,74,75,69,49])

n = int(input("Enter your roll no. => "))

print("Your Maths mark is => ", maths[n])
print("Your Economic mark is => ",eco[n])


