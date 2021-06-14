from collections import deque

def insert_left(d):
    l = (input("Enter the numbers to insert : "))
    d.appendleft(l)

def insert_right(d):
    l = (input("Enter the numbers to insert : "))
    d.append(l)
def delete_left(d):
    d.popleft()
def delete_right(d):
    d.pop()

# Driver code 
d = deque(input("Enter the numbers : "))
print(d)
while(True):
    print("""
    1 -- insert-left
    2 -- insert-right
    3 -- delete -left
    4 -- delete-right
    5 -- extend
    6 -- print
    7 -- Exit
    """)
    ch = int(input("Enter the choice : "))
    if ch == 1:
        insert_left(d)
    elif ch==2:
        insert_right(d)
    elif ch ==3:
        delete_left(d)
    elif ch ==4:
        delete_right(d)
    elif ch==5:
        Extend(d)
    elif ch==6:
        print(d)
    elif ch == 7:
        exit()
    else:
        print("Invalid choice")