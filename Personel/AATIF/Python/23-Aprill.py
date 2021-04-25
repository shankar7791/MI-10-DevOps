d = {101 : "Aatif", 102 : "Anjali", 103 : "Avdhooth", 104 : "Chandrakar", 105 : "Chetan"}

while (True) :

    print(''' 
    1. Add
    2.Show
    3.Delete
    4.Update
    5.Search
    6.Exit''')
    ch = int(input("Enter Choice: "))
   
    if ch == 1 :
        roll_no = int(input("Enter The Roll No.: "))
        name = str(input("Enter The Name Of Candidate: "))
        d[roll_no] = name
        print("\nAdded Information Successfully!!")
   
    elif ch == 2 :
        for i in d:
            print(i, ":", d[i])
   
    elif ch == 3 :
        roll_no = int(input("Enter the Roll No.: "))
        del(d[roll_no])
        print("Deleted Information Successfully!!!")
   
    elif ch == 4 :
        roll_no = int(input("Enter the Roll No.: "))
        print("Name of Candidate is: ", d[roll_no])
        name = str(input("Update name of candidate: "))
        d = {roll_no:name}
        print("Updated Name: ", d[roll_no])
        print("Updated Information successfully!!!")
   
    elif ch == 5 :
        roll_no = int(input("Enter the Roll No.: "))
        if roll_no in d :
            print("Name Of Candidate: ", d[roll_no])
            print("Record Found!!!")
        else :
            print("Record Not Found!!!!")
   
    elif ch == 6 :
        exit()
    else :
        print("Invalid Choice")