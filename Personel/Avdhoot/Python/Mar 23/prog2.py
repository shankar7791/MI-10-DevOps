'''
Write a Python class which has two methods get_String and print_String. 
get_String accept a string from the user and print_String print the string in upper case
'''

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