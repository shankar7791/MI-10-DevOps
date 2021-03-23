# Write a Python class to reverse a string word by word.
# Input string : 'hello my name is dev'
# Expected Output : '.dev is name my hello'

class str_rev:

    def r_words(self,w):
        return ' '.join(reversed(w.split()))

print(str_rev().r_words('hello my name is dev'))