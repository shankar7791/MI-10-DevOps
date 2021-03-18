

list1 = []
n = int(input("Enter the numbers of elements you want to add : "))
for i in range(n) :
    add = int(input())
    list1.append(add)
print(list1)

while True :

    print("""
1. Insert
2. Display
3. Delete
4. Update
5. Exit

""")

# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> Choice of operations >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

    ch = int(input("Enter your choice : "))

# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> Adding Element >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
    if ch == 1 :
        l = int(input("Enter number to add : "))
        list1.append(l)
        print("Updated List =>",list1)

# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> Display List >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
    elif ch == 2 :
        print("List => ",list1)

# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> Deleting Elements >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

    elif ch == 3 :
        print("List => ",list1)
        l = int(input("Enter number to delete : "))
        list1.remove(l)
        print("Updated list => ",list1)


# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> Updating Elements >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

    elif ch == 4 :
        print("List => ",list1)
        update = int(input("In which index you want to update : "))
        n = int(input("Enter number to update : "))
        list1[update] = n
        print("List Updated => ",list1)
     
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> Exit >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

    elif ch == 5 :
        print("Good Bye")
        exit()

    else :
        print("Please Enter A Valid Input !!!!!")

