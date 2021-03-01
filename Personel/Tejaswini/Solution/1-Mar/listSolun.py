#Solution of list using user input  

list1 = []
i=0
n = int(input("Enter number of elements in the list : "))

while i<n:
   print(f"Enter element No-{i+1}: ")
   elm = (input())
   list1.append(elm) 
   i=i+1
print(f"The entered list is: {list1}")

if list1[0] == list1[n-1]:
    print(True) #if 1st element is equal to last element
else:
    print(False)