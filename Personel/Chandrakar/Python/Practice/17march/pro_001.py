def Inse_rt(s):
    add = int(input("Enter the Insert value : "))
    list1.append(add)
    pr = print(list1)
    return pr
def dis_play(s):
    de = int(input("Enter the number which one is delet : "))
    list1.remove(de)
    pr = print(list1)
    return pr
def upd_at(s):
    up = int(input("Enter the index number which one is update : "))
    list1[up]=int(input("Enter the value : "))
    pr3 = print(list1)
    return pr3    
n = int(input("Enter the list : "))
list1 = []
for i in range(n):
    n1 = int(input("Enter the values in a list : "))
    list1.append(n1)

print("\n",list1) 
while True:
    print("""   
    1. Insert
    2. Display
    3. Delet
    4. Update
    5. Exit 
    """.upper())   
    choice = int(input("Enter the choice opration : "))
    if choice == 1:
        Inse_rt(choice)
    elif choice == 2:
        print(list1)
    elif choice == 3:
       dis_play(choice)
    elif choice == 4:
       upd_at(choice)
    elif choice == 5:
        print("Exit")
        break  

    else:
        print(" Invalid Input ")
          