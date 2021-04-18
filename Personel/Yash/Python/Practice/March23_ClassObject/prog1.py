class school :
    def __init__(self,name,address,id) :
        self.name = name
        self.address = address
        self.id = id

sc = school("DVMK","Khed",123)
print("School Name : ",sc.name)
print("Address : ",sc.address)
print("Id : ",sc.id)