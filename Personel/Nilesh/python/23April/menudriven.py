d = {1 : "Nilesh", 2 : "Mayur", 3 : "Nil", 4 : "siddhesh"}

def add():
    n = int(input("\nEnter Your Roll Number => "))
    s = input("\nEnter Your Name => ")
    d[n] = s

def Delete():
    n = int(input("\nEnter Your Roll Number = "))

    d.pop(n)

def SHOW():
    for i in d :
        print("Display Info")
        print(i, "=", d[i])

def Undate():
    n = int(input("\nEnter Your Roll Number => "))

    s = input("\nEnter Your Updated Name => ")
    up = {n:s}
    d.update(up)

def Search():
    n = int(input("\nEnter Roll Number => "))
    print(d.get(n))


while True :
    print("""
    1. ADD
    2. SHOW
    3. Delete
    4. Update
    5. Search
    6. Exit
    """)


    ch = int(input("\nEnter Your Choice => "))

    if ch == 1 :
        add()

    elif ch == 2 :
        SHOW()


    elif ch == 3 :
        Delete()

    elif ch == 4 : 
        Undate()


    elif ch == 5 :
        Search()

    elif ch == 6 :
        exit()

    else :
        print("Invalid Input ")
