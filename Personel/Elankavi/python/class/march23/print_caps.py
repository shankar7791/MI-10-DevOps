# Write a Python class which has two methods ,get_String accept a string from the user and print_String print the string in upper case

class upper:
    def input(self):
        self.input=input("Enter the string : ")
    def print(self):
        return (self.input.upper())
b=upper()
b.input()
print(b.print())