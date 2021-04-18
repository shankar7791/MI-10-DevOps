class school :
    def __init__(self,name,address,id) :
        self.name = name
        self.address = address
        self.id = id
    def myFunc(self) :
        print("School Name : ",sc.name)
        print("Address : ",sc.address)
        print("Id : ",sc.id)

sc = school("DVMK","Khed",123)
sc.myFunc()
sc.address = "Pune"
print(sc.address)