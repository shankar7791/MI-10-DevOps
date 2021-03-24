#upper case to lower case change proramming
class string():
    def get_String(self):
        self.str1 = input("enter the upper case string  : ")

    def print_String(self):
        print("Upper case string is : ",self.str1.lower())

str1 = string()
str1.get_String()
str1.print_String()