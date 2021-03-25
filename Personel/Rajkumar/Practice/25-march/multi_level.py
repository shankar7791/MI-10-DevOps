class University:
    def getUdetails(self):
        self.uName = input("Enter University Name : ")
        self.uRID = input("Enter Reg. (University) No. : ")
    def showUdetails(self):
        print("University Name :", self.uName)
        print("University Reg. No. :", self.uRID)
class College(University):
    def getClgDetails(self):
        self.cName = input("Enter College Name : ")
        self.cRID = input("Enter Reg. (College) No. : ")
        self.getUdetails()
    def showClgDetails(self):
        print("College Name :", self.cName.upper())
        print("College Reg. No. :", self.cRID.upper())
        self.showUdetails()
class Student(College):
    def getStudDetails(self):
        self.sName = input("Enter Student Name : ")
        self.sRoll = input("Enter Student's Enroll No.: ")
        self.sBranch = input("Enter Student's Branch: ")
        self.getClgDetails()
    def showStudDetails(self):
        print("\nSTUDENT DETAILS", self.sName)
        print("Student Name :", self.sName.upper())
        print("Student Enroll. No. :", self.sRoll)
        print("Student Branch :", self.sBranch)
        self.showClgDetails ()
s = Student()
s.getStudDetails()
s.showStudDetails()