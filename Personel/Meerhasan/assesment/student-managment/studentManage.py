# Prog 2 : Student Management System.

# Create program for Student Management System using OOP Concepts

# Problem Statement:
# Write a program to build a simple Student Management System using Python which can perform following operations:

# Accept
# Display
# Search
# Delete
# Update
#-------------------------------------------------------------------------------------------------------------------------------------------------------
class Student_Management():

    def oprations(self):


        print("""\n -*-*-*-*-*-*-*-*--WELCOME STUDENTS--*-*-*-*-*-*-*-*--\n
        1. ADD STUDENT
        2. Display Details 
        3. Search
        4. Delete 
        5. Update 
        6. Check Your ID 
        7. Exit 

        """)

        
list1 = []
list2 = []
list3 = []
list4 = []

#-------------------------------------------------------------------------------------------------------------------------------------------------------

class accept():
    def acp(self):
        
        self.roll =  int(input("\n Enter Roll Number => "))
        self.name = input("\n Enter Your Name => ")
        self.age = int(input("\n Entter Your Age => "))
        self.stream =  input("\n Enter Your Stream => ")

        list1.append(self.name)
        list2.append(self.roll)
        list3.append(self.age)
        list4.append(self.stream)

#-------------------------------------------------------------------------------------------------------------------------------------------------------

    def display(self):
        n = int(input("\nEnter Your ID => "))
        print(f" -*-*-*-*-*-*-*-*- {list1[n].upper()}  -*-*-*-*-*-*-*-*- \n")
        print("Roll No. => ", list2[n])
        print("Name     => ", list1[n])
        print("Age      => ", list3[n])
        print("Stream   => ", list4[n])

#-------------------------------------------------------------------------------------------------------------------------------------------------------

    def Search(self):
        n = int(input("\nEnter Your ID => "))
        print(f" -*-*-*-*-*-*-*-*- {list1[n].upper()}  -*-*-*-*-*-*-*-*- \n")

        print("Roll No. => ", list2[n])
        print("Name     => ", list1[n])
        print("Age      => ", list3[n])
        print("Stream   => ", list4[n])

#-------------------------------------------------------------------------------------------------------------------------------------------------------

    def Delete(self):
        n = int(input("\nEnter Your ID => "))
        print(f"\n STUDENT {list1[n].upper()} DETAILS ARE DELETED SUCCESSFULLY... THANK YOU... !")
        list1.pop(n)
        list2.pop(n)
        list3.pop(n)
        list4.pop(n)
    
#-------------------------------------------------------------------------------------------------------------------------------------------------------

    def Update(self):
        n = int(input("\nEnter Your ID => "))
        print(f"\n-*-*-*-*-*-*-*-*-*- WELCOME {list1[n].upper()} UPDATE YOUR DETAILS -*-*-*-*-*-*-*-*-*-")
        self.name = input("\nEnter Your Updated Name => ")
        self.roll = input("\nEnter Your Updated Roll Number  => ")
        self.age = input("\nEnter Current Age  => ")
        self.stream = input("\nEnter Current Stream => ")

        list1[n] = self.name
        list2[n] = self.roll
        list3[n] = self.age
        list4[n] = self.stream

        print(f"\nTHANK YOU..! {list1[n].upper()} YOUR DETAILS UPDATED SUCCESSFULLY")

#-------------------------------------------------------------------------------------------------------------------------------------------------------

ob = Student_Management()
ob2 = accept()


while True :
    ob.oprations()
    ch = int(input("Enter Your Choise => "))
    if ch == 1 :
        
        ob2.acp()

    elif ch == 2 :
        ob2.display()

    elif ch == 3 :
        ob2.Search()
        
    elif ch == 4 :
        ob2.Delete()

    elif ch == 5 :
        ob2.Update()

    elif ch == 6 :
        n = int(input("Enter Your Roll Number => "))
        print("\nYour ID => ", list2.index(n))

    elif ch == 7 :
        exit()

    else :
        print("\nEnter A Valid Input.....!")


    