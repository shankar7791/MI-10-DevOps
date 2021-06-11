from collections import UserString

class Mystring(UserString):
    
    def append(self, s):
        self.data += s
          
    def remove(self, s):
        self.data = self.data.replace(s, "")
      
s1 = Mystring("pooja")
print("Original String:", s1.data)

s="jagtap"
s1.append("s")
print("String After Appending:", s1.data)

rev_string=""
rev_string == Mystring[::-1]
if rev_string == Mystring:
    print("string is pallindrome:")
else:
    print(" string is not palindrome")