l=[]
def create():
    n=int(input("Enter no of index  "))
    for x in range(0,n):
        ele=int(input("Enter the element  "))
        l.append(ele)
    print(l)

def display():

    print(f"list is  {l}  ")

def add():
    pos=int(input("Enter the index  "))
    ele=int(input("Enter the element  "))
    l.insert(pos,ele)
    print(l)

def update():
    pos=int(input("Enter the position of index"))
    ele=int(input("Enter the element for update  "))
    l[pos]=ele
    print(l)

def delete():
    ele=int(input("Enter the element for delete"))
    l.remove(ele)
    print(l)

    
while True:
    print("""
    1.create
    2.display
    3.add
    4.update
    5.delete
    6.exit""")
    ch=int(input("Enter Your choice  "))
    if ch==1:
        print("creat list")
        create()
    if ch==2:
        print("Display list")
        display()
    elif ch==3:
        print("insert element")
        add()
    elif ch==4:
        print("update list")
        update()
    elif ch==5:
        print("Delete element")
        delete()
    elif ch==6:
        print("exit")
        exit()
    else:
        print("Enter valid choice")
