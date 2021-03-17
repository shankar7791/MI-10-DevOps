list = ['mango','banana','cherry','apple','pineapple','watermelon']

print("***MENU*****")
print("1.Add")
print("2.update")
print("3.delete")
print("4.length")
print("5.exit")

while True:
    choice  = input("enter your choice (1/2/3/4/5): ")

    if (choice == '1','2','3','4','5'):
        if choice == '1':
            Add = input("add element : ")
            list.append(Add)
            print(list)

        if choice == '2':
            index = int(input("enter the index number : "))
            update = input("enter the value : ")
            list[index] = update
            print(list)

        if choice == '3':
            delete = int(input("enter the index number you wants to delete : "))
            del list[delete]
            print(list)

        if choice == '4':
            length = len(list)
            print(length)

        if choice == '5':
            exit()
    else:
        print("invalid choice")
