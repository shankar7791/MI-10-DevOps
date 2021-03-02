def my_function(fname):
  print("Hello"+fname)

my_function("Yash")
my_function("Raj")
my_function("Ram") 

def my_function(fname, lname):
  print(fname + " " + lname)

my_function("Yash", "Malavade") 

def my_function(*names):   #Arbitrary Arguments
  print("The youngest child is " + names[1])
  print("The oldest child is " + names[3])

my_function("Yash", "Raj", "Ram","Jack") 

def my_function(child1, child2, child3):   #Keyword Arguments
  print("The youngest child is " + child3)

my_function(child1 = "Lucy", child2 = "Yash", child3 = "Jack") 

def my_function(**name): #Arbitrary Keyword Arguments
  print("His last name is " + name["lname"])

my_function(fname = "Yash", lname = "Malavade") 