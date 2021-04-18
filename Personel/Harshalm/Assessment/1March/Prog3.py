#Given a list of numbers, return True if first and last number of a list is same

list= int(input("Enter the list of number :-"))
print(list)

first_number = list[0]
last_number = list[-1]

if first_number == last_number :
    print("True")
else :
    print("False")
