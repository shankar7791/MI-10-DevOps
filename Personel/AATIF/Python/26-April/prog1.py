stud_info = ["Name","batch", "Address", "phone no"]

def menu() :
    print("Student Information")
    print("Add Info")
    print("Show Info")
    print("Delete Info")
    print("Update Info")
    print("Search Info")
    print("Exit")

def add_info() :
    name = str(input("Enter The Name Of Candidate: "))
    batch = str(input("Enter Your Batch: "))
    addr = str(input("Enter Your Address: "))
    phn = int(input("Enter Your phone no.: "))
    stud_info["Name", "batch", "Address", "phone no"] = name, batch, addr, phn
    print("Data Added Successfully!!!!")
    input("Press Any  Key To Continue")
    return

def show() :
    print("Student Information")
    for show in stud_info :
        print(show, end = '\t |')
    input("Press any Ket To Continue")

def update():
    print("Update Student Information")
    name = input("Enter The Name to Update Info: ")
    update_info = []
    student_data = []
    for info in stud_info :
        value = input("Enter", + info + ":")
        student_data.append(value)
    update_info.append(student_data)
    input("Press Any Key To Continue")

while (True) :
    menu()
    option = input("Enter Your Option: ")
    if option == '1' :
        add_info()
    elif option == '2' :
        show()
    elif option == '3' :
        update()
    else :
        break



    