# Create menu driven Program to implement
# a. OrderedDict
# b. DefaultDict
# c. NamedTuple
# d. ChainMap

from collections import OrderedDict, defaultdict, namedtuple, ChainMap

def o_dict(d):   
    print("This is a Dict:\n") 
        
    for key, value in d.items(): 
        print(key, value) 
        
    print("\nThis is an Ordered Dict:\n") 
    od = OrderedDict(d) 
        
    for key, value in od.items(): 
        print(key, value)
    
    x = input("enter the key to delete :")
    od.pop(x)

    print('\nRe-insert the deleted key :')
    key = input("\nEnter the key : \n")
    value = input("\nEnter the value : ")

    od[key] = value
    
    print('\nAfter re-inserting')
    for key, value in od.items(): 
        print(key, value)

def def_dict(l):
    d = defaultdict(int) 
     
        
    # Iterate through the list 
    # for keeping the count 
    for i in l: 
            
        # The default value is 0 
        # so there is no need to  
        # enter the key first 
        d[i] += 1
            
    print(d)

def n_tuple(n,a,d):
    Student = namedtuple('Student',['name','age','DOB']) 
        
    # Adding values 
    S = Student(n,a,d) 
    
    print(S)
    # Access using index 
    print ("The Student age using index is : ",end ="") 
    print (S[1]) 
        
    # Access using name  
    print ("The Student name using keyname is : ",end ="") 
    print (S.name)

    # initializing iterable  
    li = [n,a,d ] 
        
    # initializing dict 
    di = { 'name' : n, 'age' : a, 'DOB' : d } 
        
    # using _make() to return namedtuple() 
    print ("The namedtuple instance using iterable is  : ") 
    print (Student._make(li)) 
        
    # using _asdict() to return an OrderedDict() 
    print ("The OrderedDict instance using namedtuple is  : ") 
    print (S._asdict())

def c_map(d1,d2,d3):
    
    
    # Defining the chainmap 
    c = ChainMap.maps(d1, d2) 
        
    # Accessing Values using key name
    print(c['a'])
    
    # Accesing values using values()
    # method
    print(c.values())
    
    # Accessing keys using keys()
    # method
    print(c.keys())
        
    # printing chainMap 
    print ("All the ChainMap contents are : ") 
    print (c) 
        
    # using new_child() to add new dictionary 
    c1 = c.new_child(d3) 
        
    # printing chainMap
    print ("Displaying new ChainMap : ") 
    print (c1)


menu = {}
menu['1']="Ordered Dict" 
menu['2']="Default Dict"
menu['3']="Named Tuple"
menu['4']="Chain Map"
menu['5']="Exit"

while True:
        options=menu.keys()
        
        print ("\nMENU")
        print("======================\n")
        for entry in options: 
            print(entry, menu[entry])
        print("")
        selection = input("\nPlease Select:\n")

        if selection == '1' :
            print ("\nAdding Initial Dictionary\n") 
            d = {}
            length = int(input("Enter the number of elements you want for your List  : \n"))
            for counter in range(0,length) :
                key = input("\nEnter the key : \n")
                value = input("\nEnter the value : ")
                d[key] = value
            o_dict(d)    
                


        elif selection == '2' :
            print ("\nAdding List\n") 
            lst = []
            length = int(input("Enter the number of elements you want for your Linked List  : \n"))
            for counter in range(0,length) :
                item = int(input("\nEnter the elements : \n"))
                lst.append(item)
            def_dict(lst)   
              

        elif selection == '3':
            n=input('enter name: ')
            a=int(input('enter the age: '))
            d=int(input('enter the dob : '))
            n_tuple(n, a, d)
            
        elif selection == '4':
            d1 = {}
            d2 = {}
            d3 = {}
            length = int(input("Enter the number of elements you want for your Dictionary  : \n"))
            for counter in range(0,length) :
                key = input("\nEnter the key : \n")
                value = input("\nEnter the value : ")
                d1[key] = value
            
            length = int(input("Enter the number of elements you want for your Dictionary  : \n"))
            for counter in range(0,length) :
                key = input("\nEnter the key : \n")
                value = input("\nEnter the value : ")
                d2[key] = value
            
            length = int(input("Enter the number of elements you want for your Dictionary  : \n"))
            for counter in range(0,length) :
                key = input("\nEnter the key : \n")
                value = input("\nEnter the value : ")
                d3[key] = value
            c_map(d1,d2,d3)

        elif selection == '5':    
            exit()
        
        else: 
            print ("\nUnknown Option Selected!") 

