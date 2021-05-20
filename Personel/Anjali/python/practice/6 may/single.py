class animal:
    def eat(self):
        print("Eating...")
        print
class Dog(animal):
    def bark(self):
        print("Barking..")
object = Dog()
object.eat()
object.bark()