# Program 1 : Write a Python class to reverse a string word by word.
# Input string : 'hello my name is dev'
# Expected Output : '.dev is name my hello

class reverse : 
    def rev(self,s) :
        split = s.split(" ")
        revStr = " ".join(reversed(split))
        return revStr


rv = reverse()
print(rv.rev("hello my name is yash"))

