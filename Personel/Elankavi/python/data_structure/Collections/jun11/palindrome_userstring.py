from collections import UserString

class string(UserString):

    def palindrome(self):
        r = self.data[::-1]
        if self.data == r:
            print("palindrome")
        else:
            print("Not  a palindrome")
    
    def concatenation(self):
        n = input("Enter the new string : ")
        r = self.data + n
        print("The concatenation : ",r)
s = string(input("Enter the string "))
s.concatenation()
s.palindrome()
