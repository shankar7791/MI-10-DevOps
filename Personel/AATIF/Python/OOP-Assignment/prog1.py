#Program to count the Number Of Instances Of Class In Python

class Inst_class:
    

    counter = 0
  

    def __init__(self):
        

        Inst_class.counter += 1
  
  
I1 = Inst_class()
I2 = Inst_class()
I3 = Inst_class()
I4 = Inst_class()
print("Number Of Instance Class: ", Inst_class.counter)