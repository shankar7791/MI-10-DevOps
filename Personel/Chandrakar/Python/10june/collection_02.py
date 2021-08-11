
# A Python program to demonstrate working of OrderedDict
from collections import OrderedDict
from collections import defaultdict
from collections import namedtuple
from collections import ChainMap  

while True :

    print("""
1. OrderedDict
2. DefaultDict
3. NamedTuple
4. ChainMap
""")

    choice = int(input("Enter the choice opration : "))
    if choice == 1 :
        while True :
            print("""
            1. Creat OrderDict
            2. Update 
            3. Delete
            4. Display
            5. Exit
            """)
            choice = int(input("Enter the choice opration : "))

            if choice == 1 :
                n = int(input("enter a  number of insert range :"))
                d = OrderedDict()

                for i in range(n):
                    keys = input("Enter the Key elements :") 
                    values = input("Enter the Values elemets :") 
                    d[keys] = values
                    print(d)
                continue
            if choice == 2 :
                n = input("enter the keys element :")
                update = input("Enter the update values : ")
                d[n] = update
                print(d)
                continue
            if choice == 3 :
                n = input("enter the keys element :")
                d.pop(n)
                print(d)
                continue
            if choice == 4 :
                print(keys, values) 
                continue
            if choice == 5 :
                
                exit()
            else :
                print("Invaild input ")
                
                
    if choice == 2 :
        while True :
            print("""
            1. Creat DefaultDict
            2. Display
            3. Exit
            """)
            choice = int(input("Enter the choice opration : ")) 
            if choice == 1 :
                n = int(input("enter the range :"))
                d = defaultdict(lambda: "Not Present")
                for i in range(n):
                    keys = input("Enter the Key elements :") 
                    values = input("Enter the Values elemets :") 
                    d[keys] = values
                    print(d)
                continue
            if choice == 2 :
                n = input("Enter the keys element : ")
                p = d[n]
                print("Values is : ", p)
            else :
                print("exit")
                exit()
    if choice == 3 :
        while True :
            print("""
            1. Create Nametuple
            2. Display
            3.exit()
            """)
            choice = int(input("enter the choice :"))
            if choice == 1 :
                Student = namedtuple('Student',['name','age','DOB'])
                name = input("Enter the name : ")
                age = input("Enter the age : ")
                dob = input("Enter the DOB : ")
                s = Student(name, age, dob)
                continue
            if choice == 2 :
                print ("The Student age using index is : ",end ="")  
                print (s[1])   
                print ("The Student name using keyname is : ",end ="")  
                print (s.name)
                continue 
            if choice == 3 :
                print("Exit")
                exit()
            else :
                print("invaild input") 

        
    if choice == 4 :
        while True :
            print("""
            1. Create Chainmap
            2. Display
            3.exit()
            """)
            choice = int(input("enter the choice :"))
            if choice == 1 :
                d1 = {}
                d2 = {}
                d3 = {}
                n = int(input("Enter the range of input dicotnory"))
                for i in range(n):
                            keys = input("Enter the Key elements :") 
                            values = input("Enter the Values elemets :") 
                            d1[keys] = values
                print("\nEnter the Dictonary 2 keys and values :")            
                for i in range(n):
                            keys = input("Enter the Key elements :") 
                            values = input("Enter the Values elemets :") 
                            d2[keys] = values
                print("\nEnter the Dictonary 3 keys and values :")               
                for i in range(n):
                            keys = input("Enter the Key elements :") 
                            values = input("Enter the Values elemets :") 
                            d3[keys] = values
                c = ChainMap(d1, d2, d3)
                continue

            if choice == 2 :
                print ("All the ChainMap contents are : ")
                print (c)
                print ("\nAll keys of ChainMap are : ")
                print (list(c.keys()))
                print ("\nAll values of ChainMap are : ")
                print (list(c.values()))
                continue
            if choice == 3 :
                exit()
            else :
                print("invaild input")    