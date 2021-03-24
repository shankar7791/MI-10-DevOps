# Python program to show that we can create 
# instance variables inside methods
  


class CSSstudents:
    stream = 'cse'
    def __init__(self,roll):
        self.roll=roll
    def setaddress(self,address):
        self.address=address
    def getaddress(self):
        return self.address
a=CSSstudents(101)
a.setaddress("noida,UP")
print("roll = ",a.roll)
a.setaddress("Noida, UP")
print("Address = ",a.getaddress()) 
print("Stream = ",a.stream)