# Implement counters on number list and string list

from collections import Counter

# declaring the list
def lst_counter(l, x):
    c = Counter(l)
    print('{} has occurred {} times'.format(x, c[x]))



lst = []
  
menu = {}
menu['1']="Add Number List" 
menu['2']="Add String List"
menu['3']="Count"
menu['4']="Exit"

while True:
        options=menu.keys()
        
        print ("\nMENU")
        print("======================\n")
        for entry in options: 
            print(entry, menu[entry])
        print("")
        selection = input("\nPlease Select:\n")

        if selection == '1' :
            print ("\nAdding Number List\n") 
            length = int(input("Enter the number of elements you want for your List  : \n"))
            for counter in range(0,length) :
                item = int(input("\nEnter the elements : \n"))
                lst.append(item)
            x = int(input('\nEnter the number to count :'))    
                


        elif selection == '2' :
            print ("\nAdding String List\n") 
            length = int(input("Enter the number of elements you want for your Linked List  : \n"))
            for counter in range(0,length) :
                item = input("\nEnter the elements : \n")
                lst.append(item)
            x = input('\nEnter the string to count :')    
              

        elif selection == '3':
            lst_counter(lst,x)
            
        elif selection == '4':
            exit()
        
        else: 
            print ("\nUnknown Option Selected!") 

