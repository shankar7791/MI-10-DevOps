# 3. Implement queue size of 7 and shwo the
# a. Size of queue
# b. Check queue is Empty or not
# c. Check queue is full or not

class Queue:

    def __init__(self):
        self.queue = []

    def is_empty(self):
        return len(self.queue) == 0

    def enqueue(self, item):
        self.queue.append(item)

    def dequeue(self):
        return self.queue.pop(0)

    def size(self):
        return len(self.queue) 

    def is_full(self, length):
        if self.size() == length:
            return True
        else:
            return False

    def printq(self):
        for i in self.queue:
            print(i)
    

q=Queue()
menu = {}
menu['1'] = "Push Data"
menu['2'] = "Pop Data"
menu['3'] = "Print Data"
menu['4'] = "Size"
menu['5'] = "Is Full"
menu['6'] = "Is Empty"
menu['7'] = "Exit"

while True:
    options=menu.keys()
    
    print("\nMENU")
    print("======================\n")
    for entry in options: 
      print (entry, menu[entry])
    print("")
    selection = input("\nPlease Select:")
    print(" ")

    if selection == '1' :
        print ("\nAdding Data\n") 
        length = 7
        for counter in range(1,length+1) :
            val=input('enter the value :')
            q.enqueue(val)


    elif selection == '2' :
        if q.is_empty():
                print('Stack is empty !!!')
        else:
            print('Popped value: ',q.dequeue())

    elif selection == '3':
        q.printq()

    elif selection == '4':
        print(q.size())
    
    elif selection == '5':
        length = 7
        print(q.is_full(length))

    elif selection == '6':
        print(q.is_empty())
            
    elif selection == '7':
        exit()

    else: 
        print ("\nUnknown Option Selected!") 