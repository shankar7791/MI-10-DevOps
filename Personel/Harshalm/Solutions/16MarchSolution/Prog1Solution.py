#Python program to interchange first and last elements in a list

#Algorithm
#step1 :- start
#step2 :-create empty list a=[]
#step3 :- when take the n number of the elements in the list and store it in a variable
#step4 :- Accept the values into the list
#step5 :- using a for loop and insert them into the list
#step6 :- using a temporary variable
#step7 :- print the newly formed list
#step8 :- exit

#program

list = []
n = int(input("Enter the number of element in the list :-"))
for x in range(0 , n) :
    element = int(input("Enter the element" + str(x+1) + ":-"))
    list.append(element)
temp = list[0]
list[0] = list[n-1]
list[n-1] = temp
print("New List is :")
print(list)


#program

list1=[int(x) for x in input("Enter Input seprated by space: ").split()]
print("Original List:",list1)
list1[0], list1[-1] = list1[-1], list1[0]
print("Output: ",list1)