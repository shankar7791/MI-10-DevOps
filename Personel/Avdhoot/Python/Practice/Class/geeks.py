# Python program to show that we can create 
# instance variables inside methods

# Class for Computer Science Student
class CSStudent:
	stream = 'cse'	
	def __init__(self, roll):
		
		# Instance Variable
		self.roll = roll		 

	# Adds an instance variable 
	def setAddress(self, address):
		self.address = address
	
	# Retrieves instance variable 
	def getAddress(self): 
		return self.address 

# Driver Code
a = CSStudent(101)
a.setAddress("Noida, UP")
print("Roll = ", a.roll)
print("Stream = ", CSStudent.stream)
print("Address = ", a.getAddress())
