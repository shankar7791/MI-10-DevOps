#to print the first and last number and the entire list :
arr=list(input("Enter the numbers : "))
print("The first number of you entered : ",arr[0])
print("The last number you entered : ",arr[-1])
print("your list is : ")
for i in range(len(arr)):
    print(arr[i],end=" ")
print()
