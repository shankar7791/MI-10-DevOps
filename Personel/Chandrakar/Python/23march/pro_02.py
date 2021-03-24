class string():
    def get_String(self):
        self.str1 = input("enter the string : ")

    def print_String(self):
        print("Upper case string is : ",self.str1.upper())

str1 = string()
str1.get_String()
str1.print_String()