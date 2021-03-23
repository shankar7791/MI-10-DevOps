class CSStudent:

	stream = 'cse'	

	def __init__(self, roll):

		self.roll = roll		 

	def setAddress(self, address):
		self.address = address

	def getAddress(self): 
		    return self.address 

a = CSStudent(101)
a.setAddress("Noida, UP")
print("roll = ",a.roll)
print("stream = ",a.stream)
print("address = ",a.getAddress())