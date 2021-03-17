# Create a menu driven Program on List
# 1. Insert
# 2. Display
# 3. Delete
# 4. Update
# 5. Exit


L1 = [x for x in input("Enter List : ").split()]  #List Input 

#Insert Functon =>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
def Insert(L1) :
    i=int(input("Enter Index : "))
    elm=input("Insert Element : ")
    L1.insert(i,elm)
    return L1 

#Display Function =>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>   
def Display(L1) :
    print("Display List =>",L1)

#Delete Function =>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
def Delete(L1) :
    i = int(input("Enter Start Index :"))
    j = int(input("Enter End Index :"))
    del L1[i : j]
    return L1

#Display Function =>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
def Update(L1):       
    ind = int(input("At what index do you want to update value : "))
    elm= input("Enter the data to update : ")
    L1[ind] = elm
    return L1

def menu(L1) :
    
    while True:
        print("""********* Select the Menu choice ***********
        1.Insert List
        2.Display List
        3.Delete Lis
        4.Update List
        5.Exit
        """)
        choice = input("Enter the choice(1/2/3/4/5): ")
        if choice in ('1', '2', '3', '4', '5'): 

            if choice == '1':
                print("\nAfter Insert =>>>>",Insert(L1))

            elif choice == '2':
                Display(L1)

            elif choice == '3':
                print("List After Delete Elemnet =>>>>", Delete(L1))
                
            elif choice == '4':
                print("Updated List =>>>>",Update(L1))

            elif choice == '5':
                exit()
        else:
            print("Invalid Input")
    
menu(L1)