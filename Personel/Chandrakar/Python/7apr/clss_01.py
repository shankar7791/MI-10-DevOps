# Student management system .

# Create program for Student Management System using OOP Concepts

# Problem Statement:
# Write a program to build a simple Student Management System using Python which can perform following operations:

# Accept
# Display
# Search
# Delete
# Update


class students:
    def choice(self):
        print("""         
                \n -*-*-*-*-*-*-*-*--  WELCOME ! --*-*-*-*-*-*-*-*--\n
        Enter your choice :
        1 - Create Student Id 
        2 - Display Student details 
        3 - Search Student
        4 - Check your Id 
        5 - Update student details
        6 - Delete student details
        7 - Exit
        : """)



roll= []
name = []
age = []
stream = []
address = []


class details():
    def add(self):

        self.roll =  int(input("\n Enter Roll Number : "))
        self.name = input("\n Enter Your Name : ")
        self.age = int(input("\n Entter Your Age : "))
        self.stream =  input("\n Enter Your Stream : ")
        self.address = input("\n Enter your address : ")

        name.append(self.name)
        roll.append(self.roll)
        age.append(self.age)
        stream.append(self.stream)
        address.append(self.address)

    def display(self):
        n = int(input("\nEnter Your ID : "))
        print(f"     \n            WELCOME {name[n].upper()}  \n")
        print("Roll No. : ", roll[n])
        print("Name     : ", name[n])
        print("Age      : ", age[n])
        print("Stream   : ", stream[n])
        print("Address   : ", address[n])



    def search(self):
        n = int(input("\nEnter Your ID : "))
        print(f"     {name[n].upper()} Details   \n")

        print("Roll No. : ", roll[n])
        print("Name     : ", name[n])
        print("Age      : ", age[n])
        print("Stream   : ", stream[n])
        print("Address   : ", address[n])

    def Delete(self):
        n = int(input("\nEnter Your ID : "))
        print(f"\n STUDENT {name[n].upper()} DETAILS ARE DELETED SUCCESSFULLY..... !")
        roll.pop(n)
        name.pop(n)
        age.pop(n)
        stream.pop(n)
        address.pop(n)

    def Update(self):
        n = int(input("\nEnter Your ID : "))
        print(f"\n    WELCOME {name[n].upper()} PLEASE UPDATE YOUR DETAILS ")
        self.name = input("\nEnter Your Updated Name : ")
        self.roll = input("\nEnter Your New Roll Number : ")
        self.age = input("\nEnter Current Age  : ")
        self.stream = input("\nEnter Current Stream : ")
        self.address = input("\n Enter your permenent address : ")

        name[n] = self.name
        roll[n] = self.roll
        age[n] = self.age
        stream[n] = self.stream
        address[n] = self.address

        print(f"\nTHANK YOU..! {name[n].upper()}  DETAILS UPDATED SUCCESSFULLY")

ob=students()
ob2=details()
while True :
    ob.choice()
    ch = int(input("Enter Your Choise : "))
    if ch == 1 :

        ob2.add()

    elif ch == 2 :
        ob2.display()

    elif ch == 3 :
        ob2.search()


    elif ch == 4 :
        n = int(input("Enter Your Roll Number : "))
        print("\nYour ID : ",roll.index(n))

    elif ch == 5 :
        ob2.Update()

    elif ch == 6 :
        ob2.Delete()


    elif ch == 7 :
        exit()

    else :
        print("\nEnter A Valid Input.....!")