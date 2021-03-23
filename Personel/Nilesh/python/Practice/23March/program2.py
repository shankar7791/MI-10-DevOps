#Write a Python class which has two methods get_String and print_String. get_String accept a string from the user and print_String print the string in upper case.

class string:
    def __init__(self):
        self.A = " "

    def get_String(self):
        self.A = input("Enter the string : ")

    def print_String(self):
        print(self.A.upper())

A = string()
A.get_String()
A.print_String()

    
    