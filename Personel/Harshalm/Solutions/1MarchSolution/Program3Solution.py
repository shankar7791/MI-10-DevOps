#Given a list of numbers, return True if first and last number of a list is same

num= input("Enter the list of number :-")
list_number = list(num)

print("The list of number :-", list_number)

if list_number[0] == list_number[-1] :
    print("True")
else :
    print("False")
