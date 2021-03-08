#Write a Python program to calculate the sum of a list of numbers using recursion.
def sum(num):
    if len(num)==0:
        return 0
    else:
        return num[0]+sum(num[1:])
list1=[]
n=int(input("Enter the size of list"))
for no in range(n):
    val=int(input("Enter the element in list"))
    list1.append(val)
print(f"list {list1}")
print(f"sum of list element is{sum(list1)}")


#Algoritham
#define a function def sum(num)
#check if len(num)==0
#return 0
#else,return num[0]+sum(num[1:])
#take a empty list list1=[]
#take a input from user for size of list
#take a for loop 
#take a input from user for list element
#put the element into the empty list using append
#print list
#print the sum of element

