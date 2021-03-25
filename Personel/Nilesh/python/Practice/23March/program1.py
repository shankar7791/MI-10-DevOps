#Write a Python class to reverse a string word by word.
#Input string : 'hello my name is dev'
#Expected Output : '.dev is name my hello'

class string:
   def reverse(self,s):
       return ' '.join(reversed(s.split()))
print(string().reverse("hello my name is dev"))

