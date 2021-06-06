ls = []
ip = int(input("Enter no. of items in a list: "))
for i in range(ip):
    ele = int(input())
    ls.append(ele)

print("Operations on List")
print("1. Show items to List")
print("2. Add items to List")
print("3. Update items to List")
print("4. Delete items to List")
print("5. Exit")

while True :
    ip1 = int(input("Enter your choice (1/2/3/4/5): "))

#Show the List>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

    if ip1 == 1:
        print("Elelments of List: ", ls)

#Add items to list>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

    elif ip1 == 2:
        a = int(input("Enter no. of items to Add in list: "))
        for j in range(a):
            ele1 = int(input())
            ls.append(ele1)
        print("After Add items to List: ", ls)

#Update items in a List>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

    elif ip1 == 3:
        print("List before Updating: ", ls)
        b = int(input("Enter item you want to Update using indexing: "))
        ls[b] = input("Enter an item: ")
        print("List after Updating: ", ls)

#Delete items in a list>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

    elif ip1 == 4:
        print("List before Delete: ", ls)
        c = int(input("Enter item you want to Delete using indexing: "))
        del ls[c]
        print("List after Deleting an item: ", ls)

#Exit>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

    elif ip1 == 5:
        print("Exit")
        exit()

    else:
        print("Invalid Input...!!")
