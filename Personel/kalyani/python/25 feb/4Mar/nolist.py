# WAP python function to sum all the nos in a list

lst = []

num= int(input("How many numbers:"))

for n in range(num):
    
    numbers = int(input(" Enter numbers:"))
    
    lst.append(numbers)
    
    print(" Sum of elements in given list is:" sum(lst))