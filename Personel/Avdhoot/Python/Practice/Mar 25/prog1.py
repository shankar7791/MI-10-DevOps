#single inheritance

class Parent:
    parent_name = ""
    child_name = ""
 
    def show_parent(self):
        print(self.parent_name)

class Child(Parent):
    def show_child(self):
        print(self.child_name)
 
 
ch1 = Child()
ch1.parent_name = "Mark"
ch1.child_name = "John"
ch1.show_parent()
ch1.show_child() 