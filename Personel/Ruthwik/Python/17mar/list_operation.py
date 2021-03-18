# Create menu driven program on list
# 1.Insert
# 2. Display
# 3. Delete
# 4. Update
# 5. Exit

def insert_ele(l):
    l.insert(n,a)
    return l

def display_list(l):
    print('The list is : ',l)

def del_ele(l):
    del l[i]
    return l

def update_ele(l):
    if i < len(l):
        l[i] = b
        return l

s=input("Enter a string : ")
l=s.split(" ")
print('The entered list is :',l)

print('1.Insert')
print('2.dlinisplay')
print('3.delete')
print('4.update')
print('5.exit')

while True:
    # Take input from the user
    choice = input("Enter choice(1/2/3/4/5): ")

    if choice in ('1', '2', '3', '4', '5'):

        if choice == '1':
            n=int(input('Enter the position of element : '))
            a=input('enter the element : ')
            print(insert_ele(l))

        elif choice == '2':
            display_list(l)

        elif choice == '3':
            i = int(input("Enter Index :"))
            print('list with deleted elements are : ',del_ele(l))

        elif choice == '4':
            i = int(input("At what index do you want to update value : "))
            b= input("Enter the data to update : ")
            print('The updated list is : ', update_ele(l))
        
        elif choice == '5':
            exit()
            break
    else:
        print('Invalid')