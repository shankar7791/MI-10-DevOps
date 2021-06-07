# 2. Implement que and perform Enque and Deque operations on queue.


class Queue:
    def __init__(self):
        self.items = []
 
    def is_empty(self):
        return self.items == []
 
    def enqueue(self, data):
            self.items.append(data)
        
 
    def dequeue(self):
        return self.items.pop(0)

    
    def print(self):
        for i in self.items:
            print(i)
    




myqueue=Queue()
menu = {}
menu['1'] = "Enqueue"
menu['2'] = "Dequeue"
menu['3'] = "Print Data"
menu['4'] = "Exit"

while True:
    options=menu.keys()
    
    print ("\nMENU")
    print("======================\n")
    for entry in options: 
      print (entry, menu[entry])
    print("")
    selection = input("\nPlease Select:")
    print(" ")

    if selection == '1' :
        print ("\nAdding Data\n") 
        length = int(input("Enter the number of elements you want for your Stack : \n"))
        for counter in range(1,length+1) :
            val=input('enter the value :')
            myqueue.enqueue(val)


    elif selection == '2' :
        if myqueue.is_empty():
                print('Stack is empty !!!')
        else:
            print('Popped value: ',myqueue.dequeue())

    elif selection == '3':
        myqueue.print()
            
    elif selection == '4':
        exit()

    else: 
        print ("\nUnknown Option Selected!") 