# Program 2 : Write a Python class which has two methods get_String and print_String. get_String 
# accept a string from the user and print_String print the string in upper case. 

class UpperCase :
    def __init__(self):
        self.str = ""

    def get_String(self) :
        self.str = input("Enter the string : ")

    def print_String(self):
        print(self.str.upper())

up = UpperCase()
up.get_String()
up.print_String()

    

