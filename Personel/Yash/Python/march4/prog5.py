# Program 5 : Write a Python program function to print the even numbers from a given list. 

def checkEven(lst) :
    for num in lst: 
        if num % 2 == 0:
            print(num,end=" ") 

lst = [] 
n = int(input("Enter number of elements : ")) 
for i in range(0, n): 
    lstInput = int(input(f"Enter the element {i+1} : ")) 
    lst.append(lstInput)

print(lst)
print("Even numbers from a given list : ")
checkEven(lst)