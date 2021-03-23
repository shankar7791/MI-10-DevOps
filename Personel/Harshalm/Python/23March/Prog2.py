#Write a Python class which has two methods get_String and print_String. get_String accept a string from the user and print_String print the string in upper case.

class upperString():
    def __init__(self):
        self.str1 = ""

    def get_String(self):
        self.str1 = input("Enter the string :-")

    def print_String(self):
        print(self.str1.upper())

str1 = upperString()
str1.get_String()
str1.print_String()
