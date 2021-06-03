class Node:
    def __init__(self,item):
        self.item = item
        self.next = None
    
class Linkedlist:
    def __init__(self):
        self.head = None

if __name__ == '__main__':
    linked_list = Linkedlist()

    linked_list.head = Node(1)
    second = Node(2)
    third = Node(3)

linked_list.head.next = second
second.next = third