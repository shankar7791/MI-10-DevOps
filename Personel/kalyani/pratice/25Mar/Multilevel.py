# Multilevel inheritance

class vechicle:
    def types(self):
        print( "parent class: types of vechicle: ")
        
class car(vechicle):
    def specs(self):
        print(" child class : four wheeler luxury car :")
        
class BMW(car):
    def manufactures(self):
        print(" child class : manufactures of car :")
        
#creating constructor
d = BMW()
d.types()
d.specs()
d.manufactures()