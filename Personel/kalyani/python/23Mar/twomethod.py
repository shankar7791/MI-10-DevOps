# Write a python class which has two method get_string and print_string get_string accept a string from the user and print_string print the string in upper case.

class String():
    def __init__(self):
        self.str = ""

    def getString(self):
        self.str = input("Enter a Sentence: ")

    def printString(self):
        return self.str.upper()

res = String()
res.getString()
print(res.printString()) 