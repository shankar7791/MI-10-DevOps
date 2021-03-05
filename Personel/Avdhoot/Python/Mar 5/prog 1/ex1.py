#Write a Python program to calculate the sum of a list of numbers using recursion
'''
Algorithm
1. Define Function
2. Apply if condition
3. Apply else condition and recusrion
4. Call the Function and print the Function
'''

def sum(list):
    if len(list) == 1 :
        return list[0]
    else :
        return list[0] + sum(list[1:])
print(sum([11,20,2,9,16]))
